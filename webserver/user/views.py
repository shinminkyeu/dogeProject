from django.shortcuts import render, redirect
from django.views import generic

from .models import User
from .forms import UserForm
from contract import checkSign
from dog.views import getBreed

# Create your views here.
def info(request):
    if request.method == 'POST':
        request.session['address'] = request.POST['address']
    try:
        if request.session['User'].user_address == request.session['address']:
            del request.session['address']
            return render('user/info.html')
        else:
            return redirect('user:sign')
    except KeyError:
        return redirect('user:sign')

def sign(request):
    if request.method == 'POST':
        try:
            if checkSign(request.POST['signed'], request.session['address']):
                request.session['User'] = User.objects.get(pk = request.session['address'])
                return redirect('user:info')
            else:
                request.session['alertMsg'] = '서명이 유효하지 않습니다.'
                return redirect('trade:index')
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
    else:
        try:
            address = request.session['address']
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
        try:
            current_user = User.objects.get(pk = address)
        except KeyError:
            request.session['alertMsg'] = '먼저 정보 등록을 해 주세요.'
            return redirect('user:join')
        return render(request, 'user/sign.html')

def logout(request):
    try:
        del request.session['User']
    except KeyError:
        pass
    request.session['alertMsg'] = '로그아웃 되었습니다.'
    return redirect('trade:index')

def join(request):
    if request == 'POST':
        try:
            del request.session['requireSign']
            if checkSign(request.POST['signed'], request.session['address']):
                request.session['User'].save()
                request.session['alertMsg'] = '정보 등록이 완료되었습니다.'
            else:
                del request.session['User']
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
            del request.session['address']
            return redirect('trade:index')
        except KeyError:
            form = UserForm(request.POST)
            if form.is_valid():
                request.session['User'] = form.save(commit = False)
                request.session['User'].user_address = request.session['address']
                request.session['requireSign'] = True
                render(request, 'user/sign.html')
    else:
        form = UserForm()
    context = {
        'doesJoin': True,
        'address': request.session['address'],
        'form': UserForm
    }
    try:
        context['alertMsg'] = request.session['alertMsg']
        del request.session['alertMsg']
    except:
        pass
    return render(request, 'user/update.html', context)

def update(request):
    pass