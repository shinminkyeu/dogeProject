from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from .models import Picture, Dog, Breed
from .templates import *
from contract import *
s3_dogImage_Path = "https://s3.ap-northeast-2.amazonaws.com/dogeproject/dog_images/"

def register(request) :
    if request.method == 'POST':
        dog = Dog.objects.create(dog_id=request.POST.get("dogId"),dog_name=request.POST.get("dogName"),dog_coat_length=request.POST.get("coatLength"),dog_coat_color=request.POST.get("coatColor"))
        images = request.FILES.getlist('dogImages')
        if images:
            for each in images:
                Picture.objects.create(dog=dog ,picture_url=each)
        return redirect(register)
    else :
        myAddress = request.session.get('account', '0x6347fb458F79309657327F8F4Da647d21d9CF530')
        context = {
            'breedList' : getBreed(),
            'mydogs'    : findMyDogs(myAddress)
        }
        return render(request, 'dog/regi.html', context)

def info(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'dog/regi.html')


def findMyDogs(_address):
    mydogsId = contract.functions.showOwnerToDog(_address).call()
    mydogs = []
    for dogId in mydogsId:
        try:
            mydogs.append(Dog.objects.get(dog_id = dogId))
        except:
            pass
    return mydogs

def findDogInDapp(_dogId):
    
    pass

def getBreed(_size=10):
    rVal = []
    breeds = Breed.objects.all()
    for each in breeds:  #0:소형견, 1:중형견, 2:대형견
        if _size == 0:
            if each.breed_size == 0:
                rVal.append([each.id, each.breed_kind, each.breed_size])
        elif _size == 1:
            if each.breed_size == 1:
                rVal.append([each.id, each.breed_kind, each.breed_size])
        elif _size == 2:
            if each.breed_size == 2:
                rVal.append([each.id, each.breed_kind, each.breed_size])
        else:
            rVal.append([each.id, each.breed_kind, each.breed_size])
    return rVal
