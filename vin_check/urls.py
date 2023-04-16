from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cars.views import CarAPIList, AddCars, LinkList, PhotosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carlist/', CarAPIList.as_view()),
    path('api/v1/carlist/<str:vin>/', CarAPIList.as_view()),
    path('api/add/cars/', AddCars.as_view()),
    path('get/all/links/', LinkList.as_view()),
    path('photo/', PhotosView.as_view())
]
