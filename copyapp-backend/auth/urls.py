from django.urls import path
from .views import GoogleLoginCallbackView

urlpatterns = [
    # ... other URL patterns for your app ...
    path('auth/google/callback/', GoogleLoginCallbackView.as_view(), name='google-login-callback'),
]
