# Generated by Django 3.0.8 on 2020-07-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200715_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='YandexNewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('pub_date', models.DateTimeField()),
                ('hash', models.CharField(max_length=100, unique=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
