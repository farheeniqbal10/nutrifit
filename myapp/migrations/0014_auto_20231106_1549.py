# Generated by Django 3.2.21 on 2023-11-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_tips_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='file',
        ),
        migrations.AddField(
            model_name='diet',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='diet',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
