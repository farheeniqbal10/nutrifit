# Generated by Django 3.2.21 on 2023-09-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20230918_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]