# Generated by Django 3.2.21 on 2023-11-06 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_batch_batch_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
