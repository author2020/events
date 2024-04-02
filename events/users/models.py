from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class specialization(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    ADMIN = 'admin'
    USER =  'user'
    ROLE_CHOICES = ((ADMIN, 'Admin'), (USER, 'User'))

    ONLINE = 'online'
    OFFLINE = 'offline'
    event_formats = ((ONLINE, 'Online'), (OFFLINE, 'Offline'))

    NO_EXPERIENCE = 'no_experience'
    MORE_1_YEAR = 'more_1_year'
    MORE_3_YEARS = 'more_3_years'
    MORE_5_YEARS = 'more_5_years'
    OTHER_EXPERIENCE = 'other_experience'
    experience_choices = ((NO_EXPERIENCE, 'No experience'),
                          (MORE_1_YEAR, 'More than 1 year'),
                          (MORE_3_YEARS, 'More than 3 years'),
                          (MORE_5_YEARS, 'More than 5 years'),
                          (OTHER_EXPERIENCE, 'Other experience'))


    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True, null=True)
    role = models.CharField(_('role'), max_length=5, choices=ROLE_CHOICES, default=USER)
    phone = models.CharField(_('phone'), max_length=15, blank=True, null=True)
    employer = models.CharField(_('employer'), max_length=100, blank=True, null=True)
    occupation = models.CharField(_('occupation'), max_length=100, blank=True, null=True)
    experience = models.CharField(_('experience'), max_length=20, choices=experience_choices, default=NO_EXPERIENCE)
    specialization = models.ForeignKey(specialization, on_delete=models.SET_NULL, blank=True, null=True)
    preferred_format = models.CharField(_('preferred format'), max_length=10, choices=event_formats, default=ONLINE)
    consent_personal_data_processing = models.BooleanField(_('consent of the personal data processing'), default=False)
    consent_personal_data_date = models.DateTimeField(_('date of the personal data consent'), blank=True, null=True)
    consent_vacancy_data_processing = models.BooleanField(_('consent of the vacancy data processing'), default=False)
    consent_vacancy_data_date = models.DateTimeField(_('date of the vacancy data consent'), blank=True, null=True)
    consent_random_coffee = models.BooleanField(_('consent to participate in random coffee'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
    

