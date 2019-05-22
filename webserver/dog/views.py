from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone

from .models import Picture, Dog

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
        img = Picture.objects.first().picture_url
        print(img)
    context = {
        'object': img
    }
    return render(request, 'index.html', context)