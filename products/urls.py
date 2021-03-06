from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('genre/', views.product_genre, name='genre'),
    path('artist/', views.product_artist, name='artist'),
    path('label/', views.product_label, name='label'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_genre/<int:genre_id>/<int:product_id>>/', views.edit_genre,
         name='edit_genre'),
    path('edit_artist/<int:artist_id>/<int:product_id>>/',
         views.edit_artist, name='edit_artist'),
    path('edit_recordlabel/<int:label_id>/<int:product_id>>/',
         views.edit_recordlabel, name='edit_recordlabel'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_recordlabel/', views.add_recordlabel, name='add_recordlabel'),
    path('add_genre/', views.add_genre, name='add_genre'),
]
