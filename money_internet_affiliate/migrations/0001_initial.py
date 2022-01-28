# Generated by Django 4.0.1 on 2022-01-27 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('codename', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InviteLinkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invitelink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_invitelink', to='money_internet_affiliate.invitelink')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='invitelink',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_invitelink', to='money_internet_affiliate.site'),
        ),
        migrations.AddField(
            model_name='invitelink',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_invitelink', to=settings.AUTH_USER_MODEL),
        ),
    ]