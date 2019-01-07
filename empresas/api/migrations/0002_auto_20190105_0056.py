# Generated by Django 2.0.3 on 2019-01-05 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
