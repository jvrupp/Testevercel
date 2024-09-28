from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Test(APIView):
    def get(self, request):
        return Response({'msg': 'Hello World!'}, status=status.HTTP_200_OK)