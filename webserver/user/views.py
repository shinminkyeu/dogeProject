from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from web3 import Web3

from .models import User
from .forms import UserForm
from dog.models import getThumbnailOfDog
from trade.models import getThumbnailOfTrade
from contract import contract, checkSign
from resources import saveAlert, isSignedForm

# 썸네일을 가져오는 함수.
def getThumbnailsFromAddress(address):
    ownerToDog = []
    for dog_id in contract.functions.showOwnerToDog(address).call():
        ownerToDog.append(getThumbnailOfDog(dog_id))
    ownerTrade = []
    for trade_id in contract.functions.showOwnerTrade(address).call():
        ownerTrade.append(getThumbnailOfTrade(trade_id))
    buyerTrade = []
    for trade_id in contract.functions.showBuyerTrade(address).call():
        buyerTrade.append(getThumbnailOfTrade(trade_id))
    thumbnails = {
        'ownerToDog': ownerToDog,
        'ownerTrade': ownerTrade,
        'buyerTrade': buyerTrade
    }
    return thumbnails

# UserForm을 저장하는 함수. 원래는 save를 오버라이드 하고 싶었다.
def saveUserForm(userForm, address):
    userModel = userForm.save(commit = False)
    userModel.user_address = address
    userModel.save()

# 로그인 상태를 확인하고, 없으면 서명을 요구하는 함수.
def verify(request):
    if request.method == 'POST':
        # 서명 데이터가 넘어왔을 경우.
        try:
            address = request.session.pop('address')
            if checkSign(request.POST['sigData'], address):
                request.session['account'] = address
                return redirect('user:info', address)
            # 서명 데이터가 일치하지 않는 경우.
            else:
                request.session['alertMsg'] = '서명 데이터가 올바르지 않습니다.'
                return redirect('trade:index')
        # 주소 데이터가 넘어왔을 경우
        except KeyError:
            try:
                address = Web3.toChecksumAddress(request.POST['address'])
                # DB에 유저가 없으면 User.DoesNotExist 예외 발생.
                User.objects.get(pk = address)
                if request.session['account'] == address:
                    return redirect('user:info', address)
                else:
                    raise KeyError
            # account 세션이 없거나 넘어온 주소와 일치하지 않으면 서명페이지로 이동.
            except KeyError:
            # 예외가 발생하면 POST 제출된 주소를 세션에 임시로 저장한 후 예외 처리 페이지로 이동.
                request.session['address'] = address
                context = {
                    'address': address
                }
                return render(request, 'user/verify.html', context)
            # DB에 유저가 없을 경우 정보 등록 페이지로 이동
            except User.DoesNotExist:
                request.session['address'] = address
                request.session['alertMsg'] = '먼저 정보를 등록해 주세요.'
                return redirect('user:join')
    # 주소를 통한 악의적 접근의 경우.
    else:
        request.session['alertMsg'] = '잘못된 접근입니다'
        return redirect('trade:index')

def info(request, user_addr):
    context = {
        'User': get_object_or_404(User, pk = user_addr),
        'Thumbnails': getThumbnailsFromAddress(user_addr)
    }
    if hash(user_addr) == hash(request.session.get('account')):
        context['owner'] = True
    context = saveAlert(context, request)
    return render(request, 'user/info.html', context)
    
def logout(request):
    request.session.clear()
    request.session['alertMsg'] = '로그아웃 되었습니다.'
    return redirect('trade:index')

def join(request):
    # 유저 작성 데이터가 넘어올 경우.
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 제출한 정보가 유효한지 확인.
        if form.is_valid():
            address = request.session.pop('address')
            if isSignedForm(form, address):
                saveUserForm(form, address)
                request.session['account'] = address
                request.session['alertMsg'] = '정보를 등록했습니다.'
                return redirect('user:info', address)
            # 사용자가 서명 데이터를 악의적으로 조작한 경우.
            else:
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
                return redirect('trade:index')
        # 제출한 정보가 올바르지 않을 경우.
        else:
            request.session['alertMsg'] = '알맞은 정보를 등록해 주세요'
    # GET 방식으로 접근할 경우, 새 폼 제공.
    else:
        form = UserForm()
    try:
        context = {
            'doesJoin': True,
            'address': request.session['address'],
            'form': form.as_p()
        }
        context = saveAlert(context, request)
    # User 버튼으로 address를 제출하지 않고, 주소로 바로 접근할 경우.
    except KeyError:
        request.session['alertMsg'] = '잘못된 접근입니다.'
        return redirect('trade:index')
    return render(request, 'user/update.html', context)

def update(request):
    # 유저 수정 데이터가 넘어온 경우
    if request.method == 'POST':
        form = UserForm(request.POST)
        # 제출한 정보가 유효한지 확인.
        if form.is_valid():
            # 서명 확인
            if isSignedForm(form, request.session['account']):
                print(form)
                saveUserForm(form, request.session['account'])
                request.session['alertMsg'] = '정보를 업데이트 했습니다.'
                return redirect('user:info', request.session['account'])
            else:
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
                return redirect('trade:index') 
        else:
            request.session['alertMsg'] = '알맞은 정보를 등록해 주세요.'
    # GET 방식으로 접근할 경우.
    else:
        try:
            form = UserForm(instance = User.objects.get(pk = request.session['account']))
        # account 세션이 있는 경우 반드시 DB에 저장된 정보가 있으므로, DoesNotExist는 고려하지 않음.
        # 로그인(account 세션) 없이 페이지에 접근하는 경우.
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
    context = {
        'address': request.session['account'],
        'form': form.as_p()
    }
    context = saveAlert(context, request)
    return render(request, 'user/update.html', context)