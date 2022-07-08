from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.
class RegisterView(APIView):
    
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)