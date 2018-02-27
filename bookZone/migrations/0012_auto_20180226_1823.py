# Generated by Django 2.0.2 on 2018-02-26 18:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookZone', '0011_auto_20180226_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='Author_Users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='Category_Users', to=settings.AUTH_USER_MODEL),
        ),
    ]