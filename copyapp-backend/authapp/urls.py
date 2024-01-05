# urls.py

from django.urls import path
from .views import google_authenticate, google_callback

urlpatterns = [
    path('auth/google/', google_authenticate, name='google-authenticate'),
    path('auth/google/callback/', google_callback, name='google-callback'),
]

