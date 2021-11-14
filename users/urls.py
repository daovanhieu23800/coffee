from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

from . import views

app_name='users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('register/', views.register,name='register'),
    ##test
    
    #path('detailaccount/<int:pk>/',views.account_detail),
    path('account/', views.accountAPIview.as_view()),
    path('account/<int:id>',views.account_detail.as_view()),
    path('account/customer/', views.customerAPIview.as_view()),
    path('account/customer/<int:id_account>', views.customer_detail.as_view()),
]
