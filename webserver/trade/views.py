from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contract import checkSign
from .models import *

# Create your views here.
def index(request):
    search = 'b'
    content = 'c'
    context = {
        # 사이드 컨텍스트 메뉴에 들어갈 콘텐츠
        'side': side,
        # 본문에 들어갈 콘텐츠
        'text': text
    }