from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_reviews, name='list_reviews'),
    path('add/<int:product_id>', views.add_review, name='add_review'),
]