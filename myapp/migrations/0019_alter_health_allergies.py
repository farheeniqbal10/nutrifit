# Generated by Django 3.2.21 on 2024-02-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20240213_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='allergies',
            field=models.CharField(default='None', max_length=500),
        ),
    ]
