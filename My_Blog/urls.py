"""My_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blog_app import views


urlpatterns = [
    path('',views.blogview,name='blogview'),
    path('create/',views.createview,name='createview'),
    path('next/',views.nextview,name='nextview'),
    path('details/<int:pk>',views.detailview,name='detailview'),
    path('edit/<int:pk>',views.editview,name='editview'),
    path('delete/<int:pk>',views.deleteview,name='deleteview'),
    path('admin/', admin.site.urls),
]
