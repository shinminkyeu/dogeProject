from django.shortcuts import render, redirect
from django.views import generic
from eth_account.messages import defunct_hash_message
import json

from .contract import contract, signData
from dog.models import *
from user.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        sigRes = request.POST['sigRes'][2:]
        address = contract.functions.checkSignature(
            signData,
            bytes.fromhex(sigRes[:64]),
            bytes.fromhex(sigRes[64:128]),
            int(sigRes[128:], 16)
        ).call()
        context = {
            'address': address
        }
        return render(request, 'w3Conn/w3Test.html', context)
    else:
        context = {

        }
    return render(request, 'w3Conn/w3Test.html')