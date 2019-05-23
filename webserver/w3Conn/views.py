from django.shortcuts import render, redirect
from django.views import generic

from .infura import contract
from dog.models import *
from user.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        sigRes = request.POST['sigRes'][2:]
        address = contract.functions.checkSignature(
            bytes(request.POST['msgParam']),
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