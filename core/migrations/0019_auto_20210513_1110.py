# Generated by Django 3.0.8 on 2021-05-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210426_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yandexnewsitem',
            name='link',
            field=models.URLField(max_length=350, unique=True),
        ),
    ]