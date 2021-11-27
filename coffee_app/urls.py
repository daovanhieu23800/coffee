from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('', views.items, name='index'),
    path('items/type1/', views.items_detail_1, name="type1"),
    path('items/type2/', views.items_detail_2, name="type2"),
    path('items/type3/', views.items_detail_3, name="type3"),
    path('items/type4/', views.items_detail_4, name="type4"),
    path('admin/',admin.site.urls)
]
