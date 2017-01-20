# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from .models import IncomingSMS, OutgoingSMS


class SMSRequestSerializer(serializers.ModelSerializer):
    MessageSid = serializers.CharField(max_length=34, required=True, source="sms_sid")
    AccountSid = serializers.CharField(max_length=34, required=True, source="account_sid")
    From = serializers.CharField(max_length=30, required=True, source="from_number")
    To = serializers.CharField(max_length=30, required=True, source="to_number")
    Body = serializers.CharField(max_length=160, required=True, source="body")
    FromCity = serializers.CharField(max_length=100, required=False, source="from_city")
    FromState = serializers.CharField(max_length=100, required=False, source="from_state")
    FromZip = serializers.CharField(max_length=30, required=False, source="from_zip")
    FromCountry = serializers.CharField(max_length=120, required=False, source="from_country")

    # @TODO Add MessagingServiceSid and NumMedia

    class Meta:
        model = IncomingSMS
        fields = [
            "MessageSid", "AccountSid", "From", "To", "Body",
            "FromCity", "FromState", "FromZip", "FromCountry"
        ]


class SMSStatusSerializer(serializers.ModelSerializer):
    SmsSid = serializers.CharField(max_length=34, required=True, source="sms_sid")
    SmsStatus = serializers.CharField(max_length=30, required=True, source="status")

    class Meta:
        model = OutgoingSMS
        fields = [
            "SmsSid", "SmsStatus"
        ]
