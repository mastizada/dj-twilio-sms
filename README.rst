dj-twilio-sms
=================

Twilio SMS Integration for Django

.. image:: https://badge.fury.io/py/dj-twilio-sms.svg
    :target: https://pypi.python.org/pypi/dj-twilio-sms/
    :alt: pypi
.. image:: https://travis-ci.org/mastizada/dj-twilio-sms.svg?branch=master
    :target: https://travis-ci.org/mastizada/dj-twilio-sms
    :alt: travis

This is fork of `nigma/django-twilio-sms` (Filip Wasilewski en[at]ig[dot]ma) as original package has stopped maintenance.

Django 1.10 support, migrations, timezone improvements.

Used for SMS messages in SiteLedger project.


Quickstart
----------

1. Install ``dj-twilio-sms`` using ``pip``.

2. Add ``dj_twilio_sms`` to ``INSTALLED_APPS`` and migrate (``manage.py migrate``).

3. Add the following url to your urlconf:

   .. code-block:: python

       url(r"^messaging/", include("dj_twilio_sms.urls")),

   this will receive confirmation callbacks for any SMS message
   that you send using ``utils.send_sms`` also will receive incoming messages.

4. Configure Twilio callback to send notifications to the above view's url. (ex: ``/messaging/reply/`` for inbound messages)

5. Configure settings:

   - TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER - copy
     credentials from the Twilio panel.

   - TWILIO_CALLBACK_USE_HTTPS - use https or not for delivery confirmation
     callback urls.

   - TWILIO_CALLBACK_DOMAIN - optionally set domain name or IP of your site
     (otherwise the server name will be extracted from the request info).

   - TWILIO_DRY_MODE - set if you want to run in test mode.


Django Version Support
----------------------

- Django 1.8, 1.9 and 1.10
- Python 2.7 and 3.5

It should work with Django 1.6 and 1.7, but you need to downgrade django-rest-framework for these versions.


License
-------

``django-twilio-sms`` and ``dj-twilio-sms`` is released under the MIT license.

Other Resources
---------------

- GitHub repository - https://github.com/mastizada/dj-twilio-sms
- PyPi Package site - https://pypi.python.org/pypi/dj-twilio-sms
