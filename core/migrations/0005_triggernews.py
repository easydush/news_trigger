# Generated by Django 3.0.8 on 2020-07-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_triggerphrase'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriggerNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('article_link', models.URLField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('rate', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('-last_update',),
            },
        ),
    ]
