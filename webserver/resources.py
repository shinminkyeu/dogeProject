from contract import *
from dog.models import *
from trade.models import *
from user.models import *

s3_Path = "https://s3.ap-northeast-2.amazonaws.com/dogeproject/"

# Session으로 alertMsg가 넘어올 경우 메시지를 제공하는 함수.
def saveAlert(context, request):
    try:
        context['alertMsg'] = request.session.pop('alertMsg')
    except:
        pass
    return context

# form의 서명을 확인하는 함수.
def isSignedForm(form, address):
    if checkSign(form.cleaned_data['sigData'], address):
        del form.fields['sigData']
        return True
    return False

def getThumbnails(kind, key):
    getFromContract = {
        'dogToOwner': contract.functions.showdogToOwner,
        'ownerToDog': contract.functions.showOwnerToDog,
        'childToParent': contract.functions.showChildToParent,
        'parentToChildren': contract.functions.showParentToChildren,
        'ownerTrade': contract.functions.showOwnerTrade,
        'buyerTrade': contract.functions.showBuyerTrade,
    }
    getFromDB = {
        'dogToOwner': getThumbnailOfUser,
        'ownerToDog': getThumbnailOfDog,
        'childToParent': getThumbnailOfDog,
        'parentToChildren': getThumbnailOfDog,
        'ownerTrade': getThumbnailOfTrade,
        'buyerTrade': getThumbnailOfTrade,
    }
    if kind in ['ownerToDog', 'ownerTrade', 'buyerTrade']:
        key = Web3.toChecksumAddress(key)
    shown_ids = getFromContract.get(kind)(key).call()
    thumbnails = []
    for each in shown_ids:
        thumbnails.append(getFromDB.get(kind)(each))
    return thumbnails

