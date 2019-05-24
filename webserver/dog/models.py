import datetime
import re

from django.db import models

# 개의 사진에 대한 이름 정책. (개 id/사진 일련번호.확장자)
def pic_name_policy(instance, filename):
    instance.dog.dog_picture_counter += 1
    instance.dog.save()
    return 'dog_images/%s/%s.%s' % (
        instance.dog.dog_id,
        instance.dog.dog_picture_counter,
        filename.split('.')[-1]
    )

# 개의 클래스.
class Dog(models.Model):
    # Contract에서 배정된 개 id
    dog_id = models.PositiveIntegerField(primary_key = True)
    # 개의 이름(String)
    dog_name = models.CharField(max_length = 100, null = True, blank = True)
    # 개 등록 사진의 일련번호
    dog_picture_counter = models.PositiveSmallIntegerField(default = 0)
    # 개 대표 사진의 일련번호 (0이면 대표사진이 없도록 해야 하나..?)
    dog_picture_represented = models.PositiveSmallIntegerField(default = 0)
    # 개의 털길이(Enum)
    dog_coat_length = models.PositiveSmallIntegerField(null = True, blank = True)
    # 개의 털색깔(String)
    dog_coat_color = models.CharField(max_length = 100, null = True, blank = True)

# 개 사진의 url 테이블.
class Picture(models.Model):
    dog = models.ForeignKey(Dog, on_delete = models.CASCADE)
    picture_url = models.ImageField(upload_to = pic_name_policy)

# 개 종류의 테이블, 운영자만 수정 가능.
class Breed(models.Model):
    breed_kind = models.CharField(max_length=100)
    breed_size = models.PositiveSmallIntegerField()