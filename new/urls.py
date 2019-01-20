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
from new import views
app_name="new"
urlpatterns = [
    re_path('index',views.index,name= "ddl"),
    re_path('tpl1', views.tpl1),
    re_path('tpl2', views.tpl2),
    re_path('tpl3', views.tpl3),
    re_path('tpl4', views.tpl4),
    re_path('user_list', views.user_list),
]

