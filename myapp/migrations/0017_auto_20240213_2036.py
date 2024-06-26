# Generated by Django 3.2.21 on 2024-02-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20240211_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='description',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='diet',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='health',
            name='medical',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tips',
            name='description',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='tips',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='experience',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='place',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='workout',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
