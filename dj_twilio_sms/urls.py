# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url
from .views import sms_status_callback_view, IncomingSMSView

urlpatterns = [
    url(r"^callback/sent/(?P<pk>\d+)/$", sms_status_callback_view, name="sms_status_callback"),
    url(r"^reply/$", IncomingSMSView.as_view(), name="sms_inbound"),
]
