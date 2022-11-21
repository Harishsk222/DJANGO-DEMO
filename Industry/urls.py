"""Industry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Factories import views
from Users.views import *

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    
    path('',login,name='login'),
    path('logout/',logout,name='logout'),

    path('home2',views.home2,name='home2'),
    path('add_report/',views.add_report,name='add_report'),



    path('home',views.home,name='home'), 

    path('banglore_list',views.Banglore_list,name='banglore_list'),
    

    path('home3',views.home3,name='home3'),
    path('madd_report/',views.madd_report,name='madd_report'),
    path('mumbai_list',views.Mumbai_list,name='mumbai_list'),


    path('home4',views.home4,name='home4'),
    path('cadd_report/',views.cadd_report,name='cadd_report'),
    path('chennai_list',views.chennai_list,name='chennai_list'),

]
