# Generated by Django 2.1.1 on 2018-10-26 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20181025_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivo',
            name='responsable',
            field=models.CharField(default='----', max_length=100),
        ),
        migrations.AddField(
            model_name='estanque',
            name='fecha_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
