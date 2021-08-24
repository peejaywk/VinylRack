from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('genre/', views.product_genre, name="genre"),
    path('artist/', views.product_artist, name="artist"),
    path('label/', views.product_label, name="label"),
]
