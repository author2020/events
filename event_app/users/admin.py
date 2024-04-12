from django.contrib import admin

from .models import User, Specialization

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'full_name',
        'phone',
        'employer',
        'occupation',
        'experience',
        'preferred_format',
        'consent_personal_data_processing',
        'consent_vacancy_data_processing',
        'consent_random_coffee',
        'profile_full',
    )
    @admin.display(description='Полное имя')
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
