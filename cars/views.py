from django.http import Http404
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car, Photos
from .serializers import CarSerializer, VinSerializer, PhotoSerializer


class CarAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class LinkListPagination(PageNumberPagination):
    page_size = 20000
    page_size_query_param = 'page_size'


class CarAPIList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Car.objects.order_by('pk')
    serializer_class = CarSerializer
    pagination_class = CarAPIListPagination

    def get_queryset(self):
        vin = self.kwargs.get('vin')
        if not vin:
            return Car.objects.order_by('pk')
        return Car.objects.filter(vin=vin)

class AddCars(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class LinkList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Car.objects.values('vin',).order_by('pk')
    serializer_class = VinSerializer
    pagination_class = LinkListPagination


class PhotosView(ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer