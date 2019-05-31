from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from web3 import Web3

from .models import User
from .forms import UserForm
from contract import contract, checkSign
from dog.models import Dog, Picture
from dog.views import getBreed

# alertMsg가 넘어올 경우 메시지를 제공하는 함수.
def saveAlert(context, request):
    try:
        context['alertMsg'] = request.session.pop('alertMsg')
    except:
        pass
    return context

def verify(request):
    if request.method == 'POST':
        # 서명 데이터가 넘어왔을 경우. (모든 과정 처리 후 세션에 임시로 저장된 주소 삭제)
        try:
            # 서명 데이터가 일치하는 경우. 
            if checkSign(request.POST['sigData'], request.session['address']):
                request.session['account'] = request.session.pop('address')
                return redirect('user:info', request.session['account'])
            # 서명 데이터가 일치하지 않는 경우.
            else:
                request.session['alertMsg'] = '서명 데이터가 올바르지 않습니다.'
                request.session.clear()
                return redirect('trade:index')
        # 주소 데이터가 넘어왔을 경우. (sigData에서 KeyError)
        except KeyError:
            try:
                # DB에 유저가 없으면 User.DoesNotExist 예외 발생.
                User.objects.get(pk = request.POST['address'])
                if request.session['account'] == request.POST['address']:
                    return redirect('user:info', request.session['account'])
                else:
                    raise KeyError
            # 예외가 발생하면 POST 제출된 주소를 세션에 임시로 저장한 후 예외 처리 페이지로 이동.
            # account 세션이 없거나 넘어온 주소와 일치하지 않으면 서명페이지로 이동.
            except KeyError:
                request.session['address'] = request.POST['address']
                context = {
                    'address': request.session['address']
                }
                return render(request, 'user/verify.html', context)
            # DB에 유저가 없을 경우 정보 등록 페이지로 이동
            except User.DoesNotExist:
                request.session['address'] = request.POST['address']
                request.session['alertMsg'] = '먼저 정보를 등록해 주세요.'
                return redirect('user:join')
    # 주소를 통한 악의적 접근의 경우.
    else:
        request.session['alertMsg'] = '잘못된 접근입니다'
        return redirect('trade:index')

def info(request, user_addr):
    current_user = get_object_or_404(User, pk = user_addr)
    context = { 'User': current_user }
    if hash(user_addr) == hash(request.session.get('account')):
        context['owner'] = True
    dog_ids = contract.functions.showOwnerToDog(Web3.toChecksumAddress(user_addr)).call()
    if len(dog_ids):
        dogs = []
        for id in dog_ids:
            dog = Dog.objects.get(pk = id)
            dog_dict = { 'name': dog.dog_name }
            if dog.dog_picture_represented:
                dog_object['picture'] = Picture.objects.get(pk = dog.dog_picture_represented)
            dogs.append(dog_dict)
        context['Dogs'] = dogs
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
            # 서명 데이터 확인.
            if checkSign(form.cleaned_data['sigData'], request.session['address']):
                del form.fields['sigData']
                newUser = form.save(commit = False)
                newUser.user_address = request.session['address']
                # 유저를 DB에 저장한 후, 자동 로그인.
                newUser.save()
                request.session['account'] = request.session['address']
                request.session['alertMsg'] = '정보를 등록했습니다.'
                return redirect('user:info', request.session.pop('address'))
            # 사용자가 서명 데이터를 악의적으로 조작한 경우.
            else:
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
                del request.session['address']
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
        print('포스트로옴')
        form = UserForm(request.POST)
        # 제출한 정보가 유효한지 확인.
        if form.is_valid():
            print('밸리드함')
            # 서명 확인
            if checkSign(form.cleaned_data['sigData'], request.session['account']):
                print('서명됨')
                del form.fields['sigData']
                modUser = form.save(commit = False)
                modUser.user_address = request.session['account']
                modUser.save()
                request.session['alertMsg'] = '정보를 업데이트 했습니다.'
                return redirect('user:info', request.session['account'])
            else:
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
                return redirect('trade:index') 
        else:
            print('안밸리드함')
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