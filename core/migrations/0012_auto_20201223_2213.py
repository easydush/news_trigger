# Generated by Django 3.1.2 on 2020-12-23 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_vkgroup_vk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vkgroup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vkgroup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vkgroup',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vkgroup',
            name='photo_100',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vkgroup',
            name='site',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vkgroup',
            name='vk_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='vkpost',
            name='address',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vkpost',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vksource',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]