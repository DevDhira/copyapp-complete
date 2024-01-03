from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from social_django.utils import psa
from .serializers import GoogleLoginSerializer

class GoogleLoginCallbackView(APIView):
    @psa('social:complete')
    def post(self, request, backend):
        serializer = GoogleLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
