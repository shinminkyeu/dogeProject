# Generated by Django 2.2.1 on 2019-05-17 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_kind', models.CharField(max_length=100)),
                ('breed_size', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='dog_coat_color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dog',
            name='dog_coat_length',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture_url',
            field=models.ImageField(upload_to=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dog.Dog')),
        ),
    ]
