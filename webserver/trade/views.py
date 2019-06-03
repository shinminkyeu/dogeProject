from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django import forms

from contract import contract
from .models import *
from resources import *

# Create your views here.
class searchForm(forms.Form):
    gender_choice = ((False, '수컷'), (True, '암컷'))
    breed = forms.TypedChoiceField(coerce = int)
    ageStart = forms.IntegerField(min_value = 0)
    ageEnd = forms.IntegerField(min_value = 0)
    gender = forms.TypedChoiceField(choices = gender_choice, coerce = bool)



def index(request):
    context = {
        # 사이드 컨텍스트 메뉴에 들어갈 콘텐츠
    }
    waitingTrades = getWaitingTrades()
    if waitingTrades:
        context['waitingTrades'] = waitingTrades
    saveAlert(context, request)
    return render(request, 'index.html', context = context)