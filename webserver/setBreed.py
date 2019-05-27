import os
import django
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
django.setup()
from dog.models import Breed

class BreedClass :
    def __init__(self, _breed, _size):
        self.breed = _breed
        self.size = _size                   #0,소형,1:중형,2:대형

smallDogList = ['포메라니안','치와와','미니어처 핀셔','파피용','토이 푸들','미니어처 닥스훈트','요크셔 테리어','말티즈','비숑 프리제','미니어처 슈나우저','페키니즈','꼬똥 드 툴레아','재퍼니스 친', '아펜핀셔', '토이 폭스테리어', '브리셀 그리펀', '볼로네즈', '소형견 믹스']
middleDogList = ['퍼그','웰시코기','프렌치 불도그','비글','코카 스파니엘','보스턴 테리어','셔틀랜드 쉽독','이탈리안 그레이하운드','스코티시 테리어','중형견 믹스']
bigDogList = ['사모예드','셰퍼드','세인트버나드','차우차우','그레이트 데인','라브라도어','허스키','골든리트리버','대형견 믹스']
def setBreedTable() :
    b_list = []
    for each in smallDogList:
        b_list.append(BreedClass(each, 0))
    for each in middleDogList:
        b_list.append(BreedClass(each, 1))
    for each in bigDogList:
        b_list.append(BreedClass(each, 2))
    return b_list

if __name__=='__main__':
    dogList = setBreedTable()
    for each in dogList :
        Breed(breed_kind=each.breed, breed_size=each.size).save()

