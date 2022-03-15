"""menubuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from main.views import *
from log_and_reg.views import *
from recipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wel/', ReactView.as_view(), name="something"),
    path('wel2/', MenuView.as_view(), name="what"),
    #problem with DayView because there is no actual data to serialize...
    path('wel3/', DayView.as_view(), name="day"),
    path('wel4/', TagView.as_view(), name="tag"),
    path('wel5/', RecipeView.as_view(), name='recipe'),
    path('wel6/', RecipeTypeView.as_view(), name='type'),
    path('wel7/', PhotoView.as_view(), name='photo',)
]
