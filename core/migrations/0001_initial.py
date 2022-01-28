# Generated by Django 4.0.1 on 2022-01-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('h1', models.CharField(default='', max_length=200, unique=True)),
                ('head_title', models.CharField(max_length=68, unique=True, verbose_name='Meta Title / Window Title')),
                ('meta_description', models.CharField(max_length=155, unique=True, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(max_length=255, verbose_name='Meta Keywords')),
                ('meta_robots', models.CharField(choices=[('index, follow', 'All'), ('noindex, nofollow', 'None'), ('noindex, follow', 'No index, Follow'), ('index, nofollow', 'Index, No follow'), ('index', 'Index'), ('follow', 'Follow'), ('noindex', 'No index'), ('nofollow', 'No follow')], default='index, follow', max_length=100, verbose_name='Meta Robots')),
                ('type', models.CharField(choices=[('dynamic', 'Dynamic'), ('static', 'Static')], default='dynamic', max_length=100, verbose_name='Type of page')),
                ('slug', models.CharField(max_length=1000, unique=True)),
                ('status', models.CharField(choices=[('unpublished', 'Unpublished'), ('scheduled', 'Scheduled'), ('published', 'Published')], default='unpublished', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]