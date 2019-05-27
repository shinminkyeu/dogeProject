from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from .models import Picture, Dog, Breed
from .templates import *
s3_dogImage_Path = "https://s3.ap-northeast-2.amazonaws.com/dogeproject/dog_images/"
# Contract에 보낼 model.
class DogInput(models.Model):
    # birth는 템플릿에서 Date로 받은 후 unixtime으로 변경해 Contract에 전송.
    birth = models.DateField()
    # breed는 uint형으로 contract에 보관하고 구체적 정보는 DB에 저장
    breed = models.IntegerField()
    # gender는 템플릿에서 기본 Input으로 받지 않고 Radio 타입으로 받자.
    gender = models.BooleanField()
    # 생사 정보는 Contract에는 보내되 Input으로 받지는 않는다.
    alive = models.BooleanField(default=True)

def show_img(request):
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        dog = Dog.objects.get(dog_id=2)
        Picture.objects.create(dog=dog ,picture_url=img)
        return redirect(show_img)
    else:
        imgpath = Picture.objects.first().picture_url
        imgurl = imgpath
    context = {
        'path'   : s3_dogImage_Path,
        'picture': imgurl
    }
    return render(request, 'dogs/index.html', context)

def register(request) :
    if request.method == 'POST':
        pass
    else :
        context = {
            'breedList'  : getBreed()
        }
        return render(request, 'dog/regi.html', context)

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
