# Generated by Django 3.0.8 on 2020-07-15 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='yandexnewstopic',
            unique_together={('name', 'rss_url')},
        ),
    ]