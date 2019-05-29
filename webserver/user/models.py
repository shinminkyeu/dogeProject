from django.db import models
from django.core.validators import RegexValidator

# DB에 저장할 사용자 정보.
class User(models.Model):
    # 지갑 주소를 기준으로 사용자 정보 저장.
    user_address = models.CharField(max_length=42, primary_key=True)
    # 사용자 이름.
    user_name = models.CharField(max_length=10)
    # 전화번호 validator
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="휴대전화 번호는 -를 빼고 숫자로 적어 주세요.")
    # 사용자 전화번호.
    user_contact = models.CharField(max_length=15, validators=[phone_regex])