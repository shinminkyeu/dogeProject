from django.shortcuts import render, redirect
from django.views import generic

from .infura import web3
from dog.models import *
from user.models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        return redirect(request)
    else:
        context = {

        }
    return render(request, 'w3Conn/w3Test.html')