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
