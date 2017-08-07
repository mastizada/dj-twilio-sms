# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from twilio.twiml.messaging_response import MessagingResponse, Body

from .decorators import twilio_view
from .models import OutgoingSMS
from .serializers import SMSRequestSerializer, SMSStatusSerializer

logger = logging.getLogger("dj-twilio-sms.views")


class TwilioView(View):
    """
    Base view for Twilio callbacks
    """
    response_text = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TwilioView, self).dispatch(request, *args, **kwargs)

    def get_data(self):
        return self.request.POST

    def post(self, request, *args, **kwargs):
        data = self.get_data()
        return self.handle_request(data)

    def handle_request(self, data):
        return self.get_response(data)

    def get_response_text(self):
        return self.response_text

    def get_response(self, message, **kwargs):
        response = MessagingResponse()

        response_text = self.get_response_text()
        if response_text:
            response.message(response_text)

        response = HttpResponse(response.to_xml(), content_type='application/xml')
        return response


class IncomingSMSView(TwilioView):
    """Base view for handling incoming SMS messages.

    @NOTE Configure url in the Twilio admin panel.
    @NOTE Override this class' post_save function to add custom logic.
    """
    object = None

    def handle_request(self, data):
        logger.debug("Received SMS message: %r", data)

        serializer = SMSRequestSerializer(data=data)
        if serializer.is_valid():
            self.object = serializer.save()
            self.post_save()
        else:
            logger.error(
                "Failed validation of received SMS message: %s",
                serializer.errors,
                extra={"request": self.request}
            )
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        return self.get_response(message=self.object, data=data)

    def post_save(self):
        pass


class SMSStatusCallbackView(SingleObjectMixin, TwilioView):
    """Callback view for tracking status of sent messages.

    @NOTE Configure callback url in the Twilio admin panel.
    """
    object = None

    model = OutgoingSMS

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(SMSStatusCallbackView, self).post(request, *args, **kwargs)

    def handle_request(self, data):
        logger.debug("Callback for sent SMS message status %s: %r", self.object.pk, data)

        serializer = SMSStatusSerializer(instance=self.object, data=data)
        if serializer.is_valid():
            self.object = serializer.save(force_update=True)
            self.post_save()
            logger.debug(
                "Updated message status %s, %s: %s",
                self.object.pk, self.object.sms_sid, self.object.status
            )
        else:
            logger.error(
                "Failed SMS status callback: %s",
                serializer.errors,
                extra={"request": self.request}
            )
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        return self.get_response(message=self.object)

    def post_save(self):
        pass

sms_status_callback_view = twilio_view(SMSStatusCallbackView.as_view())
