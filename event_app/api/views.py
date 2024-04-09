from datetime import datetime
import pytz

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from event_app.settings import TIME_ZONE
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
        if self.action == 'list':
            if self.request.query_params.get('status') == 'upcoming':
                now = datetime.now(tz=pytz.timezone(TIME_ZONE))
                return Event.objects.filter(event_status='on_time', datetime__gt=now).order_by('datetime')
            elif self.request.query_params.get('status') == 'past':
                now = datetime.now(tz=pytz.timezone(TIME_ZONE))
                return Event.objects.filter(event_status='on_time', datetime__lte=now).order_by('-datetime')
            elif self.request.query_params.get('status') == 'scheduled':
                return Event.objects.filter(event_status='scheduled')
            elif self.request.query_params.get('status') == 'canceled':
                return Event.objects.filter(event_status='canceled')
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
