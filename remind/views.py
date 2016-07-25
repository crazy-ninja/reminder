# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from remind.serializers import RemindMeSerializer


@api_view(['POST'])
def remind_me(request):
    if not request.data.get('mobile') and not request.data.get('email'):
        return Response('Please enter either email or mobile', status=400)
    serializer = RemindMeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
