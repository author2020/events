from rest_framework import serializers
from django.utils import timezone

from events.models import Event, Subevent, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для спикера.
    '''
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Speaker
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class SubeventSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для части программы.
    '''
    subevents = SpeakerSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('event',)
        model = Subevent


class EventSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для мероприятия.
    '''
    event_status = serializers.SerializerMethodField()
    subevents = SubeventSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def get_event_status(self, obj):
        if obj.datetime <= timezone.now():
            return 'Прошедшие события'
        else:
            return 'Скоро'
