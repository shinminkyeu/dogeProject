# Generated by Django 2.2.1 on 2019-05-27 06:47

from django.db import migrations, models
import django.db.models.deletion
import trade.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepOne', models.CharField(max_length=10)),
                ('stepTwo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('trade_title', models.CharField(max_length=200)),
                ('trade_value', models.PositiveIntegerField(default=0)),
                ('trade_text', models.TextField()),
                ('trade_img_counter', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TradeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to=trade.models.img_name_policy)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.Trade')),
            ],
        ),
    ]
