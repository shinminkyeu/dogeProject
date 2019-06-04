from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.utils import timezone

from .models import *
from trade.models import RegionTable
from user.models import User
from contract import *
from resources import *

def getThumbnailsFromDogId(dog_id):
    dogToOwner = []
    for user_id in contract.functions.showDogToOwner(dog_id).call():
        dogToOwner.append(User.objects.get(pk = user_id).user_name)
    childToParent = {}
    mom_id, dad_id = contract.functions.showChildToParent(dog_id).call()
    if mom_id:
        childToParent['mom'] = getThumbnailOfDog(mom_id)
    if dad_id:
        childToParent['dad'] = getThumbnailOfDog(dad_id)
    parentToChildren = []
    for child_id in contract.functions.showParentToChildren(dog_id).call():
        parentToChildren.append(getThumbnailOfDog(child_id))
    thumbnails = {
        'dogToOwner': dogToOwner,
        'childToParent': childToParent,
        'parentToChildren': parentToChildren
    }
    return thumbnails

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

def info(request, dog_id):
    if request.method == 'POST':
        pass
    else:
        dogDapp, dogDB, dogPicture = findDog(dog_id)
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
    dogInfo = get_object_or_404(Dog, pk = _dogId)
    dogPoto = Picture.objects.filter(dog = dogInfo)
    dogPotos = []
    for each in dogPoto:
        temp = ""
        temp = s3_Path+str(each.picture_url)
        dogPotos.append(temp)
    return dogInfo, dogPotos


