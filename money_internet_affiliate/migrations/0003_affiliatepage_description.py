# Generated by Django 3.1 on 2022-02-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_internet_affiliate', '0002_auto_20220206_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliatepage',
            name='description',
            field=models.TextField(default='Hola mundo esta es la descripcion'),
            preserve_default=False,
        ),
    ]