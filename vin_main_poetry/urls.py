"""
URL configuration for vin_main_poetry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from cars.views import CarAPIList, AddCars, LinkList, CarAPIList_v2, get_brands, get_models, get_links

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carlist/', CarAPIList.as_view()),
    path('api/v1/carlist/<str:vin>/', CarAPIList.as_view()),
    path('api/add/cars/', AddCars.as_view()),
    path('get/all/links/', LinkList.as_view()),
    path('api/v2/brand/', get_brands),
    path('api/v2/model/<str:brand>/', get_models),
    path('api/v2/carlist/', CarAPIList_v2.as_view()),
    path('api/v2/carlist/<str:brand>/', CarAPIList_v2.as_view()),
    path('api/v2/carlist/<str:brand>/<str:model>/', CarAPIList_v2.as_view()),
    path('api/v2/carlist/<str:brand>/<str:model>/<str:vin>/', CarAPIList_v2.as_view()),
    path('api/v2/get_links/', get_links),
]

