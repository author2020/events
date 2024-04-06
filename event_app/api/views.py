from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.utils import timezone
import pytz

from events.models import Event, Speaker
from api.serializers import (EventSerializer, SubeventSerializer,
                             SpeakerSerializer)
from api.pagination import CustomPagination


class EventViewSet(viewsets.ModelViewSet):
    '''
    Представление для работы с мероприятиями.
    '''
    serializer_class = EventSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        moscow_tz = pytz.timezone('Europe/Moscow')
        now = timezone.now().astimezone(moscow_tz)

        if self.action == 'list':

            upcoming_events = Event.objects.filter(datetime__gt=now).order_by('datetime')
            past_events = Event.objects.filter(datetime__lt=now).order_by('-datetime')

            if self.request.query_params.get('status') == 'upcoming':
                return upcoming_events
            elif self.request.query_params.get('status') == 'past':
                return past_events
            else:
                return list(upcoming_events) + list(past_events)
        else:
            return Event.objects.all()


class SubeventViewSet(viewsets.ModelViewSet):
    '''
    Представление для работы с программой мероприятия.
    '''
    serializer_class = SubeventSerializer

    def get_queryset(self):
        queryset = get_object_or_404(Event, id=self.kwargs.get('event_id'))
        return queryset.subevents.all()


class SpeakerViewSet(viewsets.ModelViewSet):
    '''
    Представление для работы со спикером
    '''
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
