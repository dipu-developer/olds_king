"""oldkng URL Configuration

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
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard,name='dashboard'),
    path('load_mrp/',views.load_mrp,name='load_mrp'),
    path('sub_cat/',views.sub_cat,name='sub_cat'),
    path('add_data/',views.add_data,name='add_data'),
    path('records/',views.records,name='records'),
    path('show_ten_data/',views.show_ten_data,name='show_ten_data'),
    path('exel_convert/',views.exel_convert,name='exel_convert'),
]
