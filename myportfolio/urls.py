from django.urls import path
from . import views

#My Porfolio Urls
urlpatterns = [
    path('', views.index, name='home')
]