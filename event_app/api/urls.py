from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, SubeventViewSet, SpeakerViewSet

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register(
    r'^events/(?P<event_id>\d+)/subevents',
    SubeventViewSet,
    basename='subevent'
)
router.register('speakers', SpeakerViewSet, basename='speaker')

urlpatterns = [
    path('', include(router.urls)),
]
