from django.db import models

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

# 거래 이미지 테이블.
class TradeImage(models.Model):
    # 이미지의 대상 거래
    trade = models.ForeignKey(Trade, on_delete = models.CASCADE)
    # 이미지의 url
    img_url = models.ImageField(upload_to = img_name_policy)

class RegionTable(models.Model):
    stepOne = models.CharField(max_length = 10)
    stepTwo = models.CharField(max_length = 10)