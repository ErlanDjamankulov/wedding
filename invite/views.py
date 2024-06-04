from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GuestResponse
from .serializers import GuestResponseSerializer
import pywhatkit as kit
import time


def send_whatsapp_message(name, message, attending, phone_number):
    formatted_message = f"Name: {name}\nMessage: {message}\nAttending: {'Yes' if attending else 'No'}"
    kit.sendwhatmsg_instantly(phone_number, formatted_message)


@api_view(['POST'])
def guest_response(request):
    if request.method == 'POST':
        serializer = GuestResponseSerializer(data=request.data)
        if serializer.is_valid():
            guest_response = serializer.save()
            phone_number = '+996700866874'  # Замените на ваш реальный номер телефона
            send_whatsapp_message(guest_response.name, guest_response.message, guest_response.attending, phone_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
