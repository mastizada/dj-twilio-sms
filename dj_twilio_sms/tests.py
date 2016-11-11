from django.test import TestCase
from django.conf import settings
from datetime import datetime
from pytz import UTC
from dj_twilio_sms import utils
from dj_twilio_sms.models import OutgoingSMS


class SmsSendingTest(TestCase):
    def test_send_sms(self):
        result = utils.send_sms(
            request=None,
            to_number=settings.TWILIO_VERIFIED_NUMBER,
            body='Test Message from tox'
        )
        self.assertTrue(isinstance(result, OutgoingSMS))
        self.assertEqual(result.status, 'queued')
        self.assertTrue(isinstance(result.sent_at, datetime))
        self.assertEqual(result.sent_at.tzinfo, UTC)
        self.assertEqual(result.created_at.tzinfo, UTC)
