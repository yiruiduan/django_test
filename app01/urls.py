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
from app01 import views

urlpatterns = [
    re_path('business/$', views.Business.as_view()),
    re_path('group-(?P<nid>\d+).html$', views.Host_list.as_view()),
    re_path('detail-(?P<nid>\w+).html$', views.detail,name="detail"),
    re_path('test_ajax', views.test_ajax),
    # path('',views.index ),
    # re_path('index_test/(\d+)/(\d+)/',views.index,name="index"),
    path('login/', views.login),
    # path('home/', views.Home.as_view()),
    # path('detail/', views.detail),
    # re_path('detail-(?P<nid>\d+).html', views.detail),
]
