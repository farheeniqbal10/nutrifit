# Generated by Django 3.2.21 on 2023-11-01 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_workout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='estimatedtime',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='health',
            name='weeklytarget',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='diet',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
