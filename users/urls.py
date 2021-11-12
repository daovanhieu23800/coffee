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
    url(r'^account/$',views.accountAPIview.as_view()),
    url(r'^account/([0-9]+)$',views.account_detail),
]
