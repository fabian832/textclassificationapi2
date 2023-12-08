from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from asgiref.sync import async_to_sync, sync_to_async

# Create your views here.

class TextClassification(APIView):
    
    allowed_methods = ['POST']
    
    def post(self, request):
        
        # text = request.FILES['text']
        
        test="masuk"
        
        return Response({'response': test})
