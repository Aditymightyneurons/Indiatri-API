import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import random

from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
from app.models.usermodel import User

from django.db.models import Q
from datetime import datetime,timezone


sid = 'AC1dfdc46702047c8d1add009b03322731'
token = 'cbc43337eb8cf8465b527a58e7a49774'
client = Client(sid,token)
twilio_phone_number = '+46764798808'


def send_messege(phone_number):
    otp = str(random.randint(1111,9999))
    try:
        client.messages.create(
            body = otp ,
            from_ = twilio_phone_number,
            to = phone_number
        )
        return otp
    except:
        return None

def verify(phone_number):
    try:
        return User.objects.get(phone = phone_number)
    except:
        return None

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

