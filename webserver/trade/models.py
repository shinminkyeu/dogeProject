from django.db import models
from django.utils import timezone

from contract import contract, getTradeState
from resource import s3_Path
from dog.models import Dog, getRepresentedPictureOfDog
from user.models import User

# 거래 이미지에 대한 이름 정책 (거래 id/이미지 일련번호.확장자)
def img_name_policy(instance, filename):
    instance.trade.trade_img_counter += 1
    instance.trade.save()
    return 'trade_images/%s/%s.%s' % (
        instance.trade.trade_id,
        instance.trade.trade_img_counter,
        filename.split('.')[-1]
    )

# 거래에 대한 정보.
class Trade(models.Model):
    # Contract에서 받아올 거래 ID
    trade_id = models.PositiveIntegerField(primary_key = True)
    # 분양글 제목
    trade_title = models.CharField(max_length = 200)
    # 분양글 가격
    trade_value = models.PositiveIntegerField(default = 0)
    # 분양글 본문 (기본값 수정 중)
    trade_text = models.TextField()
    # 분양 이미지의 일련번호
    trade_img_counter = models.PositiveSmallIntegerField(default = 0)
    # 분양글 게시 날짜
    trade_offered_time = models.DateTimeField(default = timezone.now)

# 거래 이미지 테이블.
class TradeImage(models.Model):
    # 이미지의 대상 거래
    trade = models.ForeignKey(Trade, on_delete = models.CASCADE)
    # 이미지의 url
    img_url = models.ImageField(upload_to = img_name_policy)

class RegionTable(models.Model):
    stepOne = models.CharField(max_length = 10)
    stepTwo = models.CharField(max_length = 10)
    def __str__(self):
        return self.stepOne + ' - ' + self.stepTwo

def getThumbnailOfTrade(trade_id):
    trade = Trade.objects.get(pk = trade_id)
    dog_id = contract.functions.showTrade(trade_id).call()[0]
    trade_thumbnail = {
        'date': Trade.trade_offered_time,
        'title': Trade.trade_title,
        'state': getTradeState(trade_id)
    }
    tradeThumbnailImage = getTradeThumbnailImage(trade_id, dog_id)
    if tradeThumbnailImage:
        trade_thumbnail['image'] = tradeThumbnailImage
    return trade_thumbnail

def getWaitingTrades():
    trade_ids = contract.functions.showWaitingTrade().call()
    dog_id_index = 0
    owner_id_index = 3
    waitingTrades = []
    for trade_id in trade_ids:
        trade_in_contract = contract.functions.showTrade(trade_id).call()
        dog_id = trade_in_contract[dog_id_index]
        owner_id = trade_in_contract[owner_id_index]
        trade_thumbnail = {
            'title': Trade.objects.get(pk = trade_id).trade_title,
            'region': User.objects.get(pk = owner_id).user_region
        }
        tradeThumbnailImage = getTradeThumbnailImage(trade_id, dog_id)
        if tradeThumbnailImage:
            trade_thumbnail['image'] = tradeThumbnailImage
        waitingTrades.append(trade_thumbnail)
    return waitingTrades

def getTradeThumbnailImage(trade_id, dog_id):
    result = ''
    tradeImage = TradeImage.objects.filter(trade = trade_id)
    dog = Dog.objects.get(pk = dog_id)
    if tradeImage:
        result = s3_Path + tradeImage[0]
    else:
        dog_picture = getRepresentedPictureOfDog(Dog.objects.get(pk = dog_id))
        if dog_picture:
            result = dog_picture
    return result