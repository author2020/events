from django.contrib import admin

from .models import Event, EventRegistration, Speaker, Subevent


class EventRegistrationInline(admin.options.InlineModelAdmin):
    template = 'admin/edit_inline/yandex_events_inline.html'
    model = EventRegistration
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'format',
        'registration_status',
        'datetime',
        'registered'
    )
    list_filter = ('event_status', 'registration_status', 'format')
    search_fields = ('title__startswith',)
    ordering = ('id',)  
    fieldsets = (
        (None, {'fields': ('title', 'event_status')}),
        ('О событии', {
            'classes': ('collapse', 'wide'),
            'fields': (('organizer_name', 'organizer_contacts'),
                       ('registration_status', 'description'),
                       ('datetime', 'format', 'participant_limit'), 'image')
        }),
        ('Программа события', {
            'classes': ('collapse', 'wide'),
            'fields': ('host_full_name', 'host_contacts', 'host_company',
                       'host_position', 'host_photo')
        }),
        ('Ссылки события', {
            'classes': ('collapse', 'wide'),
            'fields': ('event_link',
                       ('online_stream_link', 'online_stream_link_start_date',
                        'online_stream_link_end_date'),
                       ('recording_link', 'recording_link_start_date',
                        'recording_link_end_date'))
        }),
    )
    list_display_links = ('title',)
    inlines = (EventRegistrationInline,)

    @admin.display(description='Зарегистрированные участники')
    def registered(self, obj):
        return obj.registrations.count()


@admin.register(Subevent)
class SubeventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'time',
    )
    list_filter = (
        'event',
        'speaker',
        'time'
    )
    fields = ('title', 'time', 'speaker')
    list_display_links = ('title',)
    ordering = ('id',)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'photo',
        'full_name',
        'contacts',
        'company',
        'position',
    )
    list_filter = (
        'company',
        'position'
    )
    fields = (
        'photo', ('first_name', 'last_name', 'contacts'), ('company', 'position',)
    )
    list_display_links = ('full_name',)
    ordering = ('id',)


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'participant',
        'event',
        'registration_date',
        'approved'
    )
    list_filter = (
        'approved',
        'registration_date'
    )
    search_fields = (
        'event__title',
        'participant__email'
    )
    list_display_links = ('participant',)
    ordering = ('id',)
