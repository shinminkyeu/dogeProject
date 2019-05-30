from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django import forms

from contract import contract, checkSign
from .models import *
from dog.models import *
from dog.views import getBreed

# Create your views here.
class searchForm(forms.Form):
    gender_choice = ((False, '수컷'), (True, '암컷'))
    breed = forms.TypedChoiceField(coerce = int)
    ageStart = forms.IntegerField(min_value = 0)
    ageEnd = forms.IntegerField(min_value = 0)
    gender = forms.TypedChoiceField(choices = gender_choice, coerce = bool)

def main(request):
    return render(request, 'trade/main.html')

def index(request):
    waiting_indexs = reversed(contract.functions.showWattingTrade().call()[-10:])
    waiting_list = []
    for id in waiting_indexs:
        waiting_list.append(contract.functions.showTrade(id).call())
    context = {
        # 사이드 컨텍스트 메뉴에 들어갈 콘텐츠
        'breeds': getBreed(),
        'searchForm': searchForm,
        # 본문에 들어갈 콘텐츠
        'waiting_list': waiting_list,
    }
    try:
        context['alertMsg'] = request.session.pop('alertMsg')
    except:
        pass
    return render(request, 'index.html', context = context)