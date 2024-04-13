from django.test import Client, TestCase

from .fixtures import EventFactory, SpeakerFactory, SubeventFactory, UserFactory
from events.models import Event, Speaker, Subevent
from users.models import User


class TestEventViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventFactory.create(title='Test event past 1', datetime='2010-10-10 00:00:00')
        EventFactory.create(title='Test event past 2', datetime='2015-10-10 00:00:00')
        EventFactory.create(title='Test event future 1', datetime='2025-10-10 00:00:00')
        EventFactory.create(title='Test event future 2', datetime='2030-10-10 00:00:00')
        EventFactory.create(title='Test event scheduled', event_status='scheduled')
        EventFactory.create(title='Test event canceled', event_status='canceled', datetime='2025-10-10 00:00:00')

    def setUp(self):
        self.client = Client()

    def test_event_list_url(self):
        response = self.client.get('/api/v1/events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 6)

    def test_event_list_url_upcoming(self):
        response = self.client.get('/api/v1/events/?status=upcoming')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 2)
        self.assertEqual(response.json()['results'][0]['title'], 'Test event future 1')
        self.assertEqual(response.json()['results'][1]['title'], 'Test event future 2')
        self.assertEqual(response.json()['results'][0]['event_status'], 'on_time')
        self.assertEqual(response.json()['results'][1]['event_status'], 'on_time')
        self.assertLessEqual(response.json()['results'][0]['datetime'],
                                response.json()['results'][1]['datetime'])

    def test_event_list_url_past(self):
        response = self.client.get('/api/v1/events/?status=past')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 2)
        self.assertEqual(response.json()['results'][0]['title'], 'Test event past 2')
        self.assertEqual(response.json()['results'][1]['title'], 'Test event past 1')
        self.assertEqual(response.json()['results'][0]['event_status'], 'on_time')
        self.assertEqual(response.json()['results'][1]['event_status'], 'on_time')
        self.assertGreaterEqual(response.json()['results'][0]['datetime'],
                                response.json()['results'][1]['datetime'])

    def test_event_list_url_scheduled(self):
        response = self.client.get('/api/v1/events/?status=scheduled')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['title'], 'Test event scheduled')
        self.assertEqual(response.json()['results'][0]['event_status'], 'scheduled')

    def test_event_list_url_canceled(self):
        response = self.client.get('/api/v1/events/?status=canceled')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['title'], 'Test event canceled')
        self.assertEqual(response.json()['results'][0]['event_status'], 'canceled')


class TestSubeventViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventFactory.create()
        SpeakerFactory.create()
        event = Event.objects.first()
        speaker = Speaker.objects.first()
        SubeventFactory.create(title='Custom subevent', event=event, speaker=speaker)

    def setUp(self):
        self.client = Client()

    def test_subevent_list_url(self):
        response = self.client.get('/api/v1/events/1/subevents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['title'], 'Custom subevent')

    def test_speaker_list_url(self):
        response = self.client.get('/api/v1/speakers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['first_name'], 'Test speaker first name')
        self.assertEqual(response.json()[0]['last_name'], 'Test speaker last name')
        self.assertEqual(response.json()[0]['position'], 'Test position')
        self.assertEqual(response.json()[0]['company'], 'Test company')
        self.assertEqual(response.json()[0]['contacts'], 'Test contacts')
        self.assertIn('www.testphoto.org', response.json()[0]['photo'])


class SpeakerViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        SpeakerFactory.create()
        SpeakerFactory.create(first_name='Test speaker 2 first name', last_name='Test speaker 2 last name')
        SpeakerFactory.create(first_name='Test speaker 3 first name', last_name='Test speaker 3 last name')

    def setUp(self):
        self.client = Client()

    def test_speaker_list_url(self):
        response = self.client.get('/api/v1/speakers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]['first_name'], 'Test speaker first name')
        self.assertEqual(response.json()[0]['last_name'], 'Test speaker last name')
        self.assertEqual(response.json()[0]['position'], 'Test position')
        self.assertEqual(response.json()[0]['company'], 'Test company')
        self.assertEqual(response.json()[0]['contacts'], 'Test contacts')
        self.assertIn('www.testphoto.org', response.json()[0]['photo'])


class EventRegistrationViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventFactory.create()
        cls.event = Event.objects.first()
        UserFactory.create(email="notparticipant@example.com")
        UserFactory.create(email="participant@example.com")
        UserFactory.create(email="secondparticipant@example.com")
        UserFactory.create(email="adminuser@example.com", role='admin')

    def setUp(self):
        self.client = Client()
        self.notpartiicpant_token = self.client.post('/api/v1/auth/token/login/',
                                                     {"email": "notparticipant@example.com",
                                                     "password": "usertestpasSW1#"}
                                                     ).json()
        self.participant_token = self.client.post('/api/v1/auth/token/login/',
                                                  {"email": "participant@example.com",
                                                  "password": "usertestpasSW1#"}
                                                  ).json()['auth_token']
        self.admin_token = self.client.post('/api/v1/auth/token/login/',
                                            {"email": "notparticipant@example.com",
                                            "password": "usertestpasSW1#"}
                                            ).json()['auth_token']

    def test_event_registration_list_authorizing(self):
        response = self.client.get('/api/v1/events/1/registrations/')
        self.assertEqual(response.status_code, 401)

    def test_event_registration_url(self):
        response = self.client.get('/api/v1/events/1/registrations/', HTTP_AUTHORIZATION=f'Token {self.notpartiicpant_token}')
        self.assertEqual(response.status_code, 200)