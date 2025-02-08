from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import SparePart
from .serializers import SparePartSerializer
from rest_framework import serializers

# Create your views here.


class SparePartListCreateView(generics.ListCreateAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer

    def get_queryset(self):

        queryset = SparePart.objects.all()

        model = self.request.query_params.get('model')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if model:
            queryset = queryset.filter(car_model__model__iexact=model)

        if min_price:
            try:
                min_price = float(min_price)
                queryset = queryset.filter(price__gte=min_price)
            except ValueError:
                raise serializers.ValidationError({"min_price": "Invalid price format."})


        if max_price:
            try:
                min_price = float(min_price)
                queryset = queryset.filter(price__gte=min_price)
            except ValueError:
                raise serializers.ValidationError({"min_price": "Invalid price format."})

        return queryset


class SparePartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
