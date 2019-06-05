# Generated by Django 2.2.1 on 2019-05-29 06:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trade.RegionTable'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_contact',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='휴대전화 번호는 -를 빼고 숫자로 적어 주세요.', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
