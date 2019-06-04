from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django import forms

from contract import contract
from .models import *
from user.models import User
from resources import *

# Create your views here.
class searchForm(forms.Form):
    gender_choice = ((False, '수컷'), (True, '암컷'))
    breed = forms.TypedChoiceField(coerce = int)
    ageStart = forms.IntegerField(min_value = 0)
    ageEnd = forms.IntegerField(min_value = 0)
    gender = forms.TypedChoiceField(choices = gender_choice, coerce = bool)

def getThumbnailFromWaitingTrades():
    trade_ids = contract.functions.showWattingTrade().call()
    dog_id_index = 0
    owner_id_index = 3
    thumbnails = []
    for trade_id in trade_ids:
        trade_in_contract = contract.functions.showTrade(trade_id).call()
        dog_id = trade_in_contract[dog_id_index]
        owner_id = trade_in_contract[owner_id_index]
        trade_thumbnail = {
            'title': Trade.objects.get(pk = trade_id).trade_title,
            'region': User.objects.get(pk = owner_id).user_region
        }
        tradeThumbnailImage = getTradeThumbnailImage(trade_id, dog_id)
        if tradeThumbnailImage:
            trade_thumbnail['image'] = tradeThumbnailImage
        thumbnails.append(trade_thumbnail)
    return thumbnails

def index(request):
    context = {
        # 사이드 컨텍스트 메뉴에 들어갈 콘텐츠
    }
    waitingTrades = getThumbnailFromWaitingTrades()
    if waitingTrades:
        context['waitingTrades'] = waitingTrades
    saveAlert(context, request)
    return render(request, 'index.html', context = context)