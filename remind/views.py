# Create your views here.
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from remind.serializers import RemindMeSerializer


@api_view(['POST'])
def remind_me(request):
    """
      To save the Reminder, User wants to create
    :param request:
    :param mobile: 10 digit Mobile number
    :param email: EMail Address
    :param message: Any Message String (Required)
    :param date_time : date and time(Required) to send the reminder and
                       Here I am assuming the user can select the time with time interval of 30 Minute
    :return: 201 or 400
    """
    # Ensure User provides Either Email or Mobile
    if not request.data.get('mobile') and not request.data.get('email'):
        return Response('Please enter either email or mobile', status=400)
    # Ensure Email is valid
    try:
        validate_email(request.data.get('email'))
    except ValidationError:
        return Response('Enter Valid Email ID', status=400)
    # Ensure User Provides some message because sending blank reminder would not be good idea
    if not request.data.get('message'):
        return Response('Please give some message', status=400)
    serializer = RemindMeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
