from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RecipeType(models.Model):
    type_name = models.CharField(max_length=45)

class Photo(models.Model):
    photo_upload = models.ImageField