from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('getnews/',views.get_news, name="news"),
    path('getpromotions/',views.get_promotion, name="promotion"),
    path('', views.items, name='index'),
    path('admin/',admin.site.urls),
    path('news/',views.news, name = "news"),
    path('newsdetail/<int:id>/',views.news_detail, name = "newsdetail"),
    path('orderhistory/',views.orderhistory, name = "orderhistory"),
    path('items/favourite/', views.items_detail_1, name="type1"),
    path('items/coffee/', views.items_detail_2, name="type2"),
    path('items/tea/', views.items_detail_3, name="type3"),
    path('items/ice/', views.items_detail_4, name="type4"),
    path('items/snack/', views.items_detail_5, name="type5"),
    path('order/', views.order, name='order'),
    path('update_item/', views.updateItem, name='update_item'),
    path('remove_item/', views.removeItem, name='remove_item'),
    path('update_promotion/', views.update_promotion, name='update_promotion'),
    path('process_order/', views.processOrder, name='process_order'),

]
