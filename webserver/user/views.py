from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from web3 import Web3

from .models import User
from .forms import UserForm
from contract import contract, checkSign
from dog.models import Dog, Picture
from dog.views import getBreed, s3_dogImage_Path



# alertMsg가 넘어올 경우 메시지를 제공하는 함수.
def saveAlert(context, request):
    try:
        context['alertMsg'] = request.session.pop('alertMsg')
    except:
        pass
    return context

# form의 서명을 확인하는 함수.
def isSignedForm(form, address):
    if checkSign(form.cleaned_data['sigData'], address):
        del form.fields['sigData']
        return True
    return False

# UserForm을 저장하는 함수. 원래는 save를 오버라이드 하고 싶었다.
def saveUserForm(userForm, address):
    userModel = userForm.save(commit = False)
    userModel.user_address = address
    userModel.save()

# 개 한 마리의 thumbnail을 이름과 대표사진의 dict로 반환하는 함수.
def getThumbnailOfDog(dog_id):
    dog = Dog.objects.get(pk = dog_id)
    dog_thumbnail = { 'name': dog.dog_name }
    dog_pictures = Picture.objects.filter(dog = dog_id)
    if dog_pictures.exists():
        if dog.dog_picture_represented:
            dog_picture_path = dog_pictures[dog.dog_picture_represented - 1].picture_url
        else:
            dog_picture_path = dog_pictures[0].picture_url
        dog_thumbnail['picture'] = s3_dogImage_Path + dog_picture_path
    return dog_thumbnail

# 개 여러 마리의 thumbnail을 thumbnail dict의 list 형태로 반환.
def findDogsByOwner(address):
    dog_ids = contract.functions.showOwnerToDog(Web3.toChecksumAddress(address)).call()
    owned_dogs = []
    for dog_id in dog_ids:
        owned_dogs.append(getThumbnailOfDog(dog_id))
    return owned_dogs

# 거래의 날짜, 제목, 상태 리스트를 번환.
def findTradesByOwner(address):
    
    owned_trades = []


def findTradesByBuyer(address):
    bought_trades = []

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
                address = request.POST['address']
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
    current_user = get_object_or_404(User, pk = user_addr)
    context = { 'User': current_user }
    if hash(user_addr) == hash(request.session.get('account')):
        context['owner'] = True
    thumbnail_of_dogs = findDogsByOwner(user_addr)
    if thumbnail_of_dogs:
        context['Dogs'] = thumbnail_of_dogs
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