from contract import *
from dog.models import getThumbnailOfDog
from trade.models import getThumbnailOfTrade
from user.models import getThumbnailOfUser

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

def getThumbnails(kind, address):
    getFromContract = {
        'dogToOwner': contract.functions.showdogToOwner,
        'ownerToDog': contract.functions.showOwnerToDog,
        'childToParent': contract.functions.showChildToParent,
        'parentToChildren': contract.functions.showParentToChildren,
        'onwerTrade': contract.functions.showOwnerTrade,
        'buyerTrade': contract.functions.showBuyerTrade,
        'waitingTrade': contract.functions.showWaitingTrade
    }
    getFromDB = {
        'dogToOwner': getThumbnailOfUser,
        'ownerToDog': getThumbnailOfDog,
        'childToParent': getThumbnailOfDog,
        'parentToChildren': getThumbnailOfDog,
        'ownerTrade': getThumbnailOfTrade,
        'buyerTrade': getThumbnailOfTrade,
        'waitingTrade': getThumbnailOfTrade
    }
    shown_ids = getFromContract.get(kind)(Web3.toChecksumAddress(address)).call()
    thumbnails = []
    for each in shown_ids:
        thumbnails.append(getFromDB.get(kind)(each))
    return thumbnails
