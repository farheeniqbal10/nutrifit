# Generated by Django 3.2.21 on 2023-09-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230912_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
