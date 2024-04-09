from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

EVENT_STATUS_CHOICES = [
        ('on_time', 'По расписанию'),
        ('scheduled', 'Запланировано'),
        ('cancelled', 'Отменено'),
    ]

REGISTRATION_STATUS_CHOICES = [
        ('not_started', 'Регистрация еще не началась'),
        ('open', 'Идет регистрация'),
        ('closed', 'Регистрация закрыта'),
    ]

FORMAT_CHOICES = [
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    ]


class Event(models.Model):
    '''
    Модель мероприятия.
    '''

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
        max_length=20,
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
    datetime = models.DateTimeField(
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
        blank=True,
        verbose_name='Участники мероприятия'
    )
    location_address = models.CharField(
        max_length=200,
        verbose_name='Адрес места проведения мероприятия',
        blank=True,
        null=True
    )
    location_coordinates = models.CharField(
        max_length=100,
        verbose_name='Координаты места проведения мероприятия',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='events/image/',
        verbose_name='Обложка мероприятия',
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    host_photo = models.ImageField(
        upload_to='events/hosts/image/',
        verbose_name='Фото ведущего',
        blank=True,
        null=True
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
    recording_link_start_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Начало срока ссылки записи'
    )
    recording_link_end_date = models.DateTimeField(
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
    online_stream_link_start_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Начало срока ссылки трансляции'
    )
    online_stream_link_end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Конец срока ссылки трансляции'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class Speaker(models.Model):
    '''
    Модель для спикера.
    '''
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя спикера'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия спикера'
    )
    company = models.CharField(
        max_length=100,
        verbose_name='Компания спикера',
        blank=True,
        null=True
    )
    contacts = models.CharField(
        max_length=100,
        verbose_name='Контакты спикера'
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Должность спикера',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='events/speakers/image/',
        verbose_name='Фото спикера',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Subevent(models.Model):
    '''
    Модель для части программы на мероприятие.
    '''

    title = models.CharField(
        max_length=100,
        verbose_name='Название части программы'
    )
    time = models.TimeField(
        verbose_name='Время начала проведения части программы'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='subevents',
        verbose_name='Мероприятие, в котором эта часть программы'
    )

    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.CASCADE,
        related_name='subevents',
        verbose_name='Спикер, участвующий в части программы'
    )

    class Meta:
        verbose_name = 'Часть программы'
        verbose_name_plural = 'Части программы'

    def __str__(self):
        return self.title
