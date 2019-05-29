from django.shortcuts import render, redirect
from django.views import generic

from .models import User
from .forms import UserForm
from contract import checkSign
from dog.views import getBreed

# Create your views here.
def info(request):
    if request.method == 'POST':
        try:
            if checkSign(request.POST['sigData'], request.session['address']):
                request.session['account'] = request.session['address']
                del request.session['address']
                raise KeyError
            else:
                request.session['alertMsg'] = '서명 데이터가 올바르지 않습니다.'
                return redirect('trade:index')
        except KeyError:
            try:
                current_user = User.objects.get(pk = request.POST['address'])
                if request.session['account'] == request.POST['address']:
                    context = {
                        'User': current_user
                    }
                else:
                    raise KeyError
            except KeyError:
                request.session['address'] = request.POST['address']
                context = {
                    'requireSign': request.session['address']
                }
            except User.DoesNotExist:
                request.session['address'] = request.POST['address']
                request.session['alertMsg'] = '먼저 정보를 등록해 주세요.'
                return redirect('user:join')
        return render(request, 'user/info.html', context)
    else:
        request.session['alertMsg'] = '잘못된 접근입니다'
        return redirect('trade:index')

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
            form = UserForm(request.POST)
            if form.is_valid():
                if checkSign(form.cleaned_data['sigData'], request.session['address']):
                    del form.fields['sigData']
                    # print('모가 어떻게 된고지')
                    newUser = form.save(commit = False)
                    newUser.user_address = request.session['address']
                    newUser.save()
                    request.session['alertMsg'] = '정보를 등록했습니다.'
                else:
                    request.session['alertMsg'] = '유효하지 않은 서명입니다.'
                del request.session['address']
                return redirect('trade:index')
            else:
                request.session['alertMsg'] = '유효한 정보를 등록해 주세요'
        except KeyError:
            request.session['alertMsg'] = '잘못된 접근입니다.'
            return redirect('trade:index')
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