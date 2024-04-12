# Generated by Django 5.0.3 on 2024-04-12 15:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Направление работы',
                'verbose_name_plural': 'Направления работы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=5, verbose_name='Роль')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('employer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место работы')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
                ('experience', models.CharField(choices=[('no_experience', 'Нет опыта'), ('more_1_year', 'Более 1 года'), ('more_3_years', 'Более 3 лет'), ('more_5_years', 'More than 5 years'), ('other_experience', 'Other experience')], default='no_experience', max_length=20, verbose_name='Опыт работы')),
                ('preferred_format', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default='online', max_length=10, verbose_name='Предпочитаемый формат')),
                ('consent_personal_data_processing', models.BooleanField(default=False, verbose_name='Согласие об обработке персональных данных')),
                ('consent_personal_data_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата согласия об обработке персональных данных')),
                ('consent_vacancy_data_processing', models.BooleanField(default=False, verbose_name='Согласие об обработке персональных данных для предложения вакансий')),
                ('consent_vacancy_data_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата согласия об обработке персональных данных для предложения вакансий')),
                ('consent_random_coffee', models.BooleanField(default=False, verbose_name='Согласие на участие в Random Coffee')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('specialization', models.ManyToManyField(blank=True, to='users.specialization', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
