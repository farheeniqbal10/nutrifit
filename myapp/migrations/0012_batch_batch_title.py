# Generated by Django 3.2.21 on 2023-11-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_health_bmi'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='Batch_title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
