from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin #UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Specialization(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    
class User(AbstractBaseUser, PermissionsMixin):
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
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)
    preferred_format = models.CharField(_('preferred format'), max_length=10, choices=event_formats, default=ONLINE)
    consent_personal_data_processing = models.BooleanField(_('consent of the personal data processing'), default=False)
    consent_personal_data_date = models.DateTimeField(_('date of the personal data consent'), blank=True, null=True)
    consent_vacancy_data_processing = models.BooleanField(_('consent of the vacancy data processing'), default=False)
    consent_vacancy_data_date = models.DateTimeField(_('date of the vacancy data consent'), blank=True, null=True)
    consent_random_coffee = models.BooleanField(_('consent to participate in random coffee'), default=False)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
    
