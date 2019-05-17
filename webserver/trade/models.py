from django.db import models

# 거래에 대한 정보.
class Trade(models.Model):
    # Contract에서 받아올 거래 ID
    trade_id = models.PositiveIntegerField(primary_key = True)