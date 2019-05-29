from django.shortcuts import render, redirect
from django.views import generic
from django.forms.models import model_to_dict

from .models import User
from .forms import UserForm
from contract import checkSign
from dog.views import getBreed

# Create your views here.
def info(request):
    if request.method == 'POST':
        request.session['address'] = request.POST['address']
    try:
        if request.session['account'] == request.session['address']:
            del request.session['address']
            context = {
                'User': User.objects.get(pk = request.session['account'])
            }
            return render(request, 'user/info.html', context)
        else:
            return redirect('user:sign')
    except KeyError:
        return redirect('user:sign')

def sign(request):
    if request.method == 'POST':
        try:
            if checkSign(request.POST['sigData'], request.session['address']):
                request.session['account'] = request.session['address']
                return redirect('user:info')
            else:
                request.session['alertMsg'] = '서명이 유효하지 않습니다.'
                del request.session['address']
                return redirect('trade:index')
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
    else:
        try:
            User.objects.get(pk = request.session['address'])
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
        except User.DoesNotExist:
            request.session['alertMsg'] = '먼저 정보 등록을 해 주세요.'
            return redirect('user:join')
        return render(request, 'user/sign.html')

def logout(request):
    try:
        del request.session['account']
    except KeyError:
        pass
    request.session['alertMsg'] = '로그아웃 되었습니다.'
    return redirect('trade:index')

def join(request):
    if request.method == 'POST':
        try:
            tmp_user = User(**request.session['User'])
            if checkSign(request.POST['signed'], request.session['address']):
                tmp_user.save()
                request.session['alertMsg'] = '정보 등록이 완료되었습니다.'
            else:
                del request.session['User']
                request.session['alertMsg'] = '유효하지 않은 서명입니다.'
            del request.session['address']
            return redirect('trade:index')
        except KeyError:
            form = UserForm(request.POST)
            if form.is_valid():
                request.session['User'] = model_to_dict(form.save(commit = False))
                return render(request, 'user/sign.html')
            else:
                request.session['alertMsg'] = '양식에 맞게 입력해 주세요.'
    else:
        form = UserForm()
    context = {
        'doesJoin': True,
        'address': request.session['address'],
        'form': form.as_p()
    }
    try:
        context['alertMsg'] = request.session['alertMsg']
        del request.session['alertMsg']
    except:
        pass
    return render(request, 'user/update.html', context)

def update(request):
    pass