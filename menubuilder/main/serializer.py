from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'note', 'public', 'created_at', 'updated_at']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']