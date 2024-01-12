# views.py

from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

import requests

@api_view(['POST'])
def google_authenticate(request):
    # Redirect the user to Google's OAuth2 consent screen
    redirect_url = 'https://accounts.google.com/o/oauth2/auth?' \
                   'client_id=690214190021-ref78qurpiceqn4ncjkj3uboi98e5po1.apps.googleusercontent.com&' \
                   'redirect_uri=http://localhost:8000/auth/google/callback/&' \
                   'response_type=code&' \
                   'scope=email%20profile'
    return Response({'redirect':redirect_url})

@api_view(['POST'])
def google_callback(request):
    # Retrieve the authorization code from the query parameters
    try:
        #auth_code = request.GET.get('access_token')
        print(request.data)
        access_token = request.data['access_token']
        print(access_token)
        # Exchange the authorization code for an access token
        # (This step should be done securely, e.g., server-side)
        
        # Make a request to Google's token endpoint to exchange the code for an access token
        # (Note: This example does not handle errors and is simplified)
        # token_url = 'https://oauth2.googleapis.com/token'
        # token_data = {
        #     'code': auth_code,
        #     'client_id': '690214190021-ref78qurpiceqn4ncjkj3uboi98e5po1.apps.googleusercontent.com',
        #     'client_secret': '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',
        #     'redirect_uri': 'http://localhost:8000/auth/google/callback/',
        #     'grant_type': 'authorization_code',
        # }
        # response = requests.post(token_url, data=token_data)
        # token_info = response.json()

        # Use the access token to fetch user information from Google's API
        user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
        #headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
        headers = {'Authorization': f'Bearer {str(access_token)}'}
        user_info_response = requests.get(user_info_url, headers=headers)
        user_info = user_info_response.json()
        
        print(user_info)
        # Handle user registration and login logic based on user_info
        # ...
        try:
            user = User.objects.get(email = user_info['email'])
            
            print("User Already Presented")
            try:
                token = Token.objects.get(user=user)
            except Exception as e:
                token = Token.objects.create(user=user)
      
            
        except Exception as e:
            user = User.objects.create(email=user_info['email'],username=user_info['email'].split('@')[0])
            token = Token.objects.create(user=user)
        return Response({'message': 'Successfully authenticated with Google', 'token': str(token.key)})
        #return JsonResponse({'message': 'Successfully authenticated with Google'})
    except Exception as e:
        return Response({'message': 'Something Went Wrong'})

    #return redirect('http://localhost:3000/')