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
    """Модель мероприятия."""

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)

    event_status = models.CharField(
        max_length=20,
        choices=EVENT_STATUS_CHOICES
    )

    registration_status = models.CharField(
        max_length=10,
        choices=REGISTRATION_STATUS_CHOICES
    )

    organizer_name = models.CharField(max_length=100)

    organizer_contacts = models.CharField(max_length=100)

    description = models.TextField()

    date = models.DateField()
    time_msk = models.TimeField()
    datetime = models.DateTimeField(
        default=timezone.localtime(timezone.now(
        ), pytz.timezone('Europe/Moscow'))
    )

    format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES
    )

    participant_limit = models.PositiveIntegerField()

    participants = models.ManyToManyField(User)

    location_address = models.CharField(max_length=200)

    location_coordinates = models.DecimalField()

    image = models.ImageField()

    published_date = models.DateTimeField()

    host_photo = models.ImageField()

    host_full_name = models.CharField(max_length=100)

    host_contacts_telegram = models.CharField(max_length=100)

    host_company = models.CharField(max_length=100)

    host_position = models.CharField(max_length=100)

    event_link = models.URLField(max_length=200)

    recording_link = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    recording_link_start_date = models.DateField(blank=True, null=True)

    recording_link_end_date = models.DateField(blank=True, null=True)

    online_stream_link = models.URLField(
        max_length=200,
        blank=True,
        null=True
    )

    online_stream_link_start_date = models.DateField(blank=True, null=True)

    online_stream_link_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
