from django.db import models

# DB에 저장할 사용자 정보.
class User(models.Model):
    # 지갑 주소를 기준으로 사용자 정보 저장.
    user_address = models.CharField(max_length=42, primary_key=True)
    # 사용자 이름.
    user_name = models.CharField(max_length=10)
    # 사용자 전화번호.
    user_contact = models.CharField(max_length=15)