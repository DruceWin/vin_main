from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer, VinSerializer


class CarAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class LinkListPagination(PageNumberPagination):
    page_size = 20000
    page_size_query_param = 'page_size'


class CarAPIList(generics.ListAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Car.objects.order_by('pk')
    serializer_class = CarSerializer
    pagination_class = CarAPIListPagination

    def get_queryset(self):
        vin = self.kwargs.get('vin')
        if not vin:
            return Car.objects.filter(is_hidden_v2=False).order_by('pk')
        return Car.objects.filter(vin=vin, is_hidden_v2=False)


class CarAPIList_v2(generics.ListAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Car.objects.order_by('pk')
    serializer_class = CarSerializer
    pagination_class = CarAPIListPagination

    def get_queryset(self):
        brand = self.kwargs.get('brand')
        model = self.kwargs.get('model')
        vin = self.kwargs.get('vin')
        if brand and model and vin:
            return Car.objects.filter(brand=brand, model__icontains=model, vin=vin, is_hidden_v2=False).order_by('pk')
        elif brand and model:
            return Car.objects.filter(brand=brand, model__icontains=model, is_hidden_v2=False).order_by('pk')
        elif brand:
            return Car.objects.filter(brand=brand, is_hidden_v2=False).order_by('pk')
        return Car.objects.filter(is_hidden_v2=False).order_by('pk')


class AddCars(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class LinkList(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Car.objects.values('vin',).order_by('pk')
    serializer_class = VinSerializer
    pagination_class = LinkListPagination


@api_view(['GET'])
def get_brands(request):
    queryset = Car.objects.filter(is_hidden_v2=False).distinct("brand").values_list("brand")
    return Response([i[0] for i in queryset])


@api_view(['GET'])
def get_models(request, brand):
    queryset = Car.objects.filter(is_hidden_v2=False, brand=brand).distinct("model").values_list("model")
    print(queryset)
    set_of_model = set()
    for product in queryset:
        short_name_model = product[0].split()
        set_of_model.add(short_name_model[0])
    return Response(sorted(list(set_of_model)))


def get_links(request):
    if request.user.is_anonymous:
        return HttpResponseNotFound('<iframe width="560" height="315" '
                                    'src="https://www.youtube.com/embed/3xYXUeSmb-Y" '
                                    'title="YouTube video player" '
                                    'frameborder="0" allow="accelerometer; autoplay; '
                                    'clipboard-write; encrypted-media; gyroscope; '
                                    'picture-in-picture; web-share" allowfullscreen></iframe>')
    if request.method == 'POST':
        domen = (request.POST['domen'])
        queryset = Car.objects.filter(is_hidden_v2=False).values_list("brand", "model", "vin")
        with open('links.txt', 'w') as file:
            for i in queryset:
                file.write(f"{domen}/{i[0]}/{i[1].split()[0]}/{i[2]} \n")
        return FileResponse(open('links.txt', 'rb'), as_attachment=True)
    return render(request, "get_links_page.html")

