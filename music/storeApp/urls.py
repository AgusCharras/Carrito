from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),

    path('add/<int:product_id>/', views.add_product, name="Add"),
    path('remove/<int:product_id>/', views.remove_product, name="Sub"),
    path('delete/<int:product_id>/', views.delete_product, name="Del"),
    path('clean/', views.clean_cart, name="CLS"),

]


