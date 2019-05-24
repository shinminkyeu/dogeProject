from django.shortcuts import render, redirect
from django.views import generic
from eth_account.messages import defunct_hash_message
import json

from .contract import checkSign
from dog.models import *
from user.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        verified = checkSign(request.POST['sigRes'], request.POST['from'])
        context = {
            'address': verified
        }
        return render(request, 'w3Conn/w3Test.html', context)
    else:
        context = {

        }
    return render(request, 'w3Conn/w3Test.html')