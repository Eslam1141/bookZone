# Generated by Django 2.0.2 on 2018-02-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookZone', '0003_auto_20180224_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_pic',
            field=models.ImageField(default='/home/linamasoud/Documents/user.png', upload_to='images/authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_pic',
            field=models.ImageField(default='/home/linamasoud/Documents/book.png', upload_to='images/books'),
        ),
    ]
