# Generated by Django 3.2.21 on 2023-11-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_health_targetweight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='medical',
            field=models.CharField(max_length=200),
        ),
    ]
