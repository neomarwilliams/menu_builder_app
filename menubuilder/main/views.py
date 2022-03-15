from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class ReactView (APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        detail = [ {"name": detail.name, "detail": detail.detail}
        for detail in React.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class MenuView (APIView):

    serializer_class = MenuSerializer

    def get(self, request):
        detail = [ {"name": detail.name, "note": detail.note, "public": detail.public}
        for detail in Menu.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# Create your views here.
