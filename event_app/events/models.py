import pytz
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

EVENT_STATUS_CHOICES = [
        ('scheduled', 'Запланировано'),
        ('in_progress', 'В процессе'),
        ('finished', 'Завершено'),
    ]

REGISTRATION_STATUS_CHOICES = [
        ('open', 'Открыта'),
        ('closed', 'Закрыта'),
    ]

FORMAT_CHOICES = [
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    ]


class Event(models.Model):
    '''Модель мероприятия.'''

    id = models.AutoField(
        primary_key=True,
        verbose_name='ID мероприятия'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название мероприятия'
    )
    event_status = models.CharField(
        max_length=20,
        choices=EVENT_STATUS_CHOICES,
        verbose_name='Статус мероприятия'
    )
    registration_status = models.CharField(
        max_length=10,
        choices=REGISTRATION_STATUS_CHOICES,
        verbose_name='Статус регистрации'
    )
    organizer_name = models.CharField(
        max_length=100,
        verbose_name='Название организатора'
    )
    organizer_contacts = models.CharField(
        max_length=100,
        verbose_name='Контакты организатора'
    )
    description = models.TextField(
        verbose_name='Описание мероприятия'
    )
    date = models.DateField()
    time_msk = models.TimeField()
    datetime = models.DateTimeField(
        default=timezone.localtime(timezone.now(
        ), pytz.timezone('Europe/Moscow')),
        verbose_name='Дата и время начала проведения мероприятия'
    )
    format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
        verbose_name='Формат мероприятия'
    )
    participant_limit = models.PositiveIntegerField(
        verbose_name='Лимит участников'
    )
    participants = models.ManyToManyField(
        User,
        verbose_name='Участники мероприятия'
    )
    location_address = models.CharField(
        max_length=200,
        verbose_name='Адрес места проведения мероприятия'
    )
    location_coordinates = models.DecimalField(
       verbose_name='Координаты места проведения мероприятия' 
    )
    image = models.ImageField(
        verbose_name='Обложка мероприятия'
    )
    published_date = models.DateTimeField(
        verbose_name='Дата публикации'
    )
    host_photo = models.ImageField(
        verbose_name='Фото ведущего'
    )
    host_full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО ведущего'
    )
    host_contacts = models.CharField(
        max_length=100,
        verbose_name='Контакты ведущего'
    )
    host_company = models.CharField(
        max_length=100,
        verbose_name='Компания ведущего'
    )
    host_position = models.CharField(
        max_length=100,
        verbose_name='Должность ведущего'
    )
    event_link = models.URLField(
        max_length=200,
        verbose_name='Ссылка на мероприятие'
    )
    recording_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Ссылка на запись мероприятия'
    )
    recording_link_start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Начало срока ссылки записи'
    )
    recording_link_end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Конец срока ссылки записи'
    )
    online_stream_link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Ссылка на онлайн-трансляцию мероприятия'
    )
    online_stream_link_start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Начало срока ссылки трансляции'
    )
    online_stream_link_end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Конец срока ссылки трансляции'
    )

    class Meta:
        ordering = ('-datetime',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
