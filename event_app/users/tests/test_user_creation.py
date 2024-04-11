from datetime import datetime
import pytz

from django.test import TestCase
# from django.utils import timezone

from event_app.settings import TIME_ZONE
from users.models import User


class UserCreationBaseTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='testemail@example.com', password='usertestpasSW1#')
        with self.settings(TIME_ZONE='UTC'):
            User.objects.create(email='testemail2@example.com', password='usertestpasSW1#',
                                first_name='Test', last_name='User', role='user', phone='1234567890',
                                employer='TestEmployer', occupation='TestOccupation',
                                experience='more_1_year', preferred_format='offline',
                                consent_personal_data_processing=True, 
                                consent_personal_data_date=datetime(2021, 1, 5, 0, 0, tzinfo=pytz.timezone(TIME_ZONE)),
                                consent_vacancy_data_processing=True,
                                consent_vacancy_data_date=datetime(2021, 1, 6, 0, 0, tzinfo=pytz.timezone(TIME_ZONE)),
                                consent_random_coffee=True)

    def test_user_password(self):
        user = User.objects.get(email='testemail@example.com')
        self.assertEqual(user.password, 'usertestpasSW1#')

    def test_user_password_fail(self):
        user = User.objects.get(email='testemail@example.com')
        self.assertNotEqual(user.password, 'usertestpasSW1#1')

    def test_user_info(self):
        user = User.objects.get(email='testemail2@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.role, 'user')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.employer, 'TestEmployer')
        self.assertEqual(user.occupation, 'TestOccupation')
        self.assertEqual(user.experience, 'more_1_year')
        self.assertEqual(user.preferred_format, 'offline')
        self.assertEqual(user.consent_personal_data_processing, True)
        self.assertEqual(user.consent_personal_data_date, datetime(2021, 1, 5, 0, 0, tzinfo=pytz.timezone(TIME_ZONE)))
        self.assertEqual(user.consent_vacancy_data_processing, True)
        self.assertEqual(user.consent_vacancy_data_date, datetime(2021, 1, 6, 0, 0, tzinfo=pytz.timezone(TIME_ZONE)))
        self.assertEqual(user.consent_random_coffee, True)

    

# class UserCreationExtendedTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(email='testemail2@example.com', password='usertestpasSW1#')

#     def test_user_uodate_info(self):
#         user = User.objects.get(email='testemail2@example.com')
#         user.objects.update(first_name='Test', last_name='User', role='admin', phone='1234567890', employer='TestEmployer', occupation='TestOccupation')

