"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from cmdb import views


urlpatterns = [
    # path('',views.index ),
    path('login/', views.login),
    re_path('home/(\w+).html', views.Home.as_view()),
    re_path('index.html', views.index,name="index"),
    re_path('orm/(?P<status>\w+).html', views.orm),
    re_path('orm/delete-(?P<id>\d+).html', views.user_delete),
    re_path('orm/edit-(?P<id>\d+).html', views.user_edit),
    re_path('detail-(?P<id>\d+).html', views.detail),
]
