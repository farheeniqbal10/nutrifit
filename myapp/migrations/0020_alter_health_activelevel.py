# Generated by Django 3.2.21 on 2024-02-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_health_allergies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='activelevel',
            field=models.CharField(max_length=30),
        ),
    ]
