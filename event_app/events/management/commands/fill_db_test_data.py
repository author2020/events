from datetime import datetime, timedelta
import pytz
from random import randint

from django.core.management.base import BaseCommand

from event_app.settings import TIME_ZONE
from events.models import Event, Subevent, Speaker

class Command(BaseCommand):
    help = 'Fill db with test data'

    def _get_random_datetime(self, upcoming=True):
        now = datetime.now(tz=pytz.timezone(TIME_ZONE))
        if upcoming:
            return datetime(now.year, (now.month + randint(0, 4)) % 12, randint(1, 28),
                            randint(14, 22), randint(0, 59), tzinfo=pytz.timezone(TIME_ZONE))
        else:
            return datetime(now.year - 1, randint(1, 12), randint(1, 28),
                            randint(14, 22), randint(0, 59), tzinfo=pytz.timezone(TIME_ZONE))
        
    def _create_subevents_and_speakers(self, event, count):
        for i in range(count):
            subevent = Subevent.objects.create(
                title=f'Subevent {i} for {event.title}',
                time=event.datetime + timedelta(hours=i),
                event=event
            )
            speaker = Speaker.objects.create(
                first_name=f'Speaker {event}_{i}',
                last_name=f'Last name {i}_{event}',
                company=f'Company {i}',
                )
            subevent.speakers.add(speaker)

    def _create_events(self, count, subevents_count=3, upcoming=True):
        for i in range(count):
            event = Event.objects.create(
                title=f'Event {i}',
                description=f'Description for event{i}',
                datetime=self._get_random_datetime(upcoming),
                format='online',
                event_status='on_time',
                participant_limit=randint(10, 10000),
                location_address='Moscow, Arbat street, 1',
                location_coordinates='55.733836, 37.588140',
                image='Image',
                host_photo='Host photo',
                host_full_name=f'Host {i}',
                host_contacts=f'Host {i} contacts',
                host_company=f'Host {i} company',
                host_position=f'Host {i} position',
                event_link='Event link',
            )
            self._create_subevents_and_speakers(event, subevents_count)


    def handle(self, *args, **options):
        self._create_events(15, subevents_count=randint(2, 5), upcoming=True)
        self._create_events(15, subevents_count=randint(2, 5), upcoming=False)
        self.stdout.write(self.style.SUCCESS('Data filled successfully'))
