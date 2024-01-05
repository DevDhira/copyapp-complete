# views.py

from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User

import requests


def google_authenticate(request):
    # Redirect the user to Google's OAuth2 consent screen
    redirect_url = 'https://accounts.google.com/o/oauth2/auth?' \
                   'client_id=690214190021-ref78qurpiceqn4ncjkj3uboi98e5po1.apps.googleusercontent.com&' \
                   'redirect_uri=http://localhost:8000/auth/google/callback/&' \
                   'response_type=code&' \
                   'scope=email%20profile'
    return redirect(redirect_url)

def google_callback(request):
    # Retrieve the authorization code from the query parameters
    auth_code = request.GET.get('code')

    # Exchange the authorization code for an access token
    # (This step should be done securely, e.g., server-side)
    
    # Make a request to Google's token endpoint to exchange the code for an access token
    # (Note: This example does not handle errors and is simplified)
    token_url = 'https://oauth2.googleapis.com/token'
    token_data = {
        'code': auth_code,
        'client_id': '690214190021-ref78qurpiceqn4ncjkj3uboi98e5po1.apps.googleusercontent.com',
        'client_secret': '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',
        'redirect_uri': 'http://localhost:8000/auth/google/callback/',
        'grant_type': 'authorization_code',
    }
    response = requests.post(token_url, data=token_data)
    token_info = response.json()

    # Use the access token to fetch user information from Google's API
    user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    # Handle user registration and login logic based on user_info
    # ...
    if User.objects.filter(email = user_info['email']).count:
        print("User Already Presented")
    else:
        User.objects.create(email=user_info['email'])
    return JsonResponse({'message': 'Successfully authenticated with Google'})
