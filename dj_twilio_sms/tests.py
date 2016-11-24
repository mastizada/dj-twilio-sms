from django.test import TestCase, Client
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
        self.assertIsNone(result.delivered_at)
        # make fake response
        client = Client(
            HTTP_USER_AGENT='Mozilla/5.0',
            HTTP_X_TWILIO_SIGNATURE='emin'
        )
        response = client.post('/messaging/callback/sent/{pk}/'.format(pk=result.pk), {
            'MessageStatus': 'sent',
            'ApiVersion': '2010-04-01',
            'SmsSid': 'SMS9i8d7spw6o5r4k3sspt2e1s0t1i2n34',
            'SmsStatus': 'sent',
            'To': settings.TWILIO_VERIFIED_NUMBER,
            'From': settings.TWILIO_PHONE_NUMBER,
            'MessageSid': 'SMS9i8d7spw6o5r4k3sspt2e1s0t1i2n34',
            'AccountSid': settings.TWILIO_ACCOUNT_SID
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._headers['content-type'][1], 'application/xml')
        # check if sms details updated
        sms = OutgoingSMS.objects.get(pk=result.pk)
        self.assertTrue(isinstance(sms.delivered_at, datetime))
        self.assertEqual(sms.status, 'sent')
