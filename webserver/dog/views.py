from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from .models import Picture, Dog, Breed
from trade.models import RegionTable
from .templates import *
from contract import *
s3_dogImage_Path = "https://s3.ap-northeast-2.amazonaws.com/dogeproject/"

def _register(dog, images, account):
    event_filter = contract.events.newDog.createFilter(fromBlock='latest', argument_filters={'owner': account})
    print(event_filter, end = " : ")
    print(event_filter.get_all_entries())

def register(request) :
    if request.method == 'POST':
        myAddress = request.session.get('account', '0x6347fb458F79309657327F8F4Da647d21d9CF530')
        dog = Dog(dog_id=request.POST.get("dogId"),dog_name=request.POST.get("dogName"),dog_coat_length=request.POST.get("coatLength"),dog_coat_color=request.POST.get("coatColor"))
        #dog = Dog.objects.create(dog_id=request.POST.get("dogId"),dog_name=request.POST.get("dogName"),dog_coat_length=request.POST.get("coatLength"),dog_coat_color=request.POST.get("coatColor"))
        images = request.FILES.getlist('dogImages')
        _register(dog, images, myAddress)
        return redirect(register)
        #return redirect('user:info', myAddress)
        """
        dog = Dog.objects.create(dog_id=request.POST.get("dogId"),dog_name=request.POST.get("dogName"),dog_coat_length=request.POST.get("coatLength"),dog_coat_color=request.POST.get("coatColor"))
        images = request.FILES.getlist('dogImages')
        if images:
            for each in images:
                Picture.objects.create(dog=dog ,picture_url=each)
        return redirect(register)
        """
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
        dogDapp, dogDB, dogPicture = findDog(16)
        context = {
            'dogDapp' : dogDapp,
            'dogDB' :   dogDB,
            'dogPicture'    : dogPicture,
            'address'   :   RegionTable.objects.all()
        }
    return render(request, 'dog/info.html', context)


def findMyDogs(_address):
    mydogsId = contract.functions.showOwnerToDog(_address).call()
    mydogs = []
    for dogId in mydogsId:
        try:
            mydogs.append(Dog.objects.get(dog_id = dogId))
        except:
            pass
    return mydogs

def findDog(_dogId):
    returnDog = {}
    returnDog['dapp'] = _findDogInDapp(_dogId)
    returnDog['db'], returnDog['picture'] = _findDogInDB(_dogId)
    return returnDog['dapp'], returnDog['db'], returnDog['picture']

class DogDapp:
    def __init__(self, _dogInfo, _dogParent, _dogChildren, _dogTrades):
        import datetime
        _birth = datetime.datetime.fromtimestamp(_dogInfo[0])
        self.unixTime = _birth
        self.birth = _birth.strftime('%Y년 %m월 %d일')
        self.breed = _dogInfo[1]
        self.gender = _dogInfo[2]
        self.alive = _dogInfo[3]
        self.regiNo = _dogInfo[4]
        self.rfid = _dogInfo[5]
        self.mom = _dogParent[0]
        self.dad = _dogParent[1]
        self.children = _dogChildren
        self.trades = _dogTrades

def _findDogInDapp(_dogId):
    dogInfo = contract.functions.findDog(_dogId).call()
    dogParent = contract.functions.showChildToParent(_dogId).call()
    dogChildren = contract.functions.showParentToChildren(_dogId).call()
    dogTrade = []#contract.functions.showParentToChildren(_dogId).call()
    _dogObject = DogDapp(dogInfo, dogParent, dogChildren, dogTrade)
    return _dogObject

def _findDogInDB(_dogId):
    dogInfo = Dog.objects.get(dog_id = _dogId)
    dogPoto = Picture.objects.filter(dog = dogInfo)
    dogPotos = []
    for each in dogPoto:
        temp = ""
        temp = s3_dogImage_Path+str(each.picture_url)
        dogPotos.append(temp)
    return dogInfo, dogPotos

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
