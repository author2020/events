from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'event_status',
        'registration_status',
        'organizer_name',
        'organizer_contacts',
        'description',
        'datetime',
        'format',
        'participant_limit',
        'location_address',
        'location_coordinates',
        'image',
        'published_date',
        'host_photo',
        'host_full_name',
        'host_contacts',
        'host_company',
        'host_position',
        'event_link',
        'recording_link',
        'recording_link_start_date',
        'recording_link_end_date',
        'online_stream_link',
        'online_stream_link_start_date',
        'online_stream_link_end_date',
    )
