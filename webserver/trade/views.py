from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django import forms

from contract import checkSign
from .models import *
from dog.models import *

# Create your views here.
class searchForm(forms.Form):
    breed = forms.TypedChoiceField()

def index(request):
    search = 'b'
    content = 'c'
    context = {
        # 사이드 컨텍스트 메뉴에 들어갈 콘텐츠
        'search': search,
        # 본문에 들어갈 콘텐츠
        'content': content
    }