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
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = CustomPagination


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
