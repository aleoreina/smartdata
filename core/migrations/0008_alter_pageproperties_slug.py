# Generated by Django 4.0.2 on 2022-02-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_pageproperties_meta_robots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageproperties',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, unique=True),
        ),
    ]
