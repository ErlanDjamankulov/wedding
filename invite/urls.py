from django.urls import path
from .views import guest_response

urlpatterns = [
    path('api/guest-response/', guest_response, name='guest_response'),
]