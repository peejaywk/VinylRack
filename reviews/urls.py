from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_reviews, name='list_reviews'),
]