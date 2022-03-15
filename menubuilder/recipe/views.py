from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializers import *

class RecipeView (APIView):

    serializer_class = RecipeSerializer

    def get(self, request):
        detail = [{'title': detail.title, 'link': detail.link, 'created_at': detail.created_at, 'updated_at': detail.updated_at}
        for detail in Recipe.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class RecipeTypeView (APIView):

    serializer_class = RecipeTypeSerializer

    def get(self, request):
        detail = [{'type_name':detail.type_name}
        for detail in RecipeType.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = RecipeTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class PhotoView (APIView):
    
    serializer_class = PhotoSerializer

    def get(self, request):
        detail = [{'photo_upload':detail.photo_upload}
        for detail in Photo.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

