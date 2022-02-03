# Generated by Django 4.0.1 on 2022-02-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_snippetitem_snippetcollection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippetcollection',
            name='collection',
        ),
        migrations.AddField(
            model_name='snippetcollection',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippetitem',
            name='snippet_collection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='snippetcollection_snippetitem', to='core.snippetcollection'),
            preserve_default=False,
        ),
    ]
