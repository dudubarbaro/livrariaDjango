from django.shortcuts import render

from rest_framework.viewsets import ModelVielSet

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializers

class CategoriaSerializers(ModelVielSet):
    queryset = Categoria.objects.all()
    serializers_class = CategoriaSerializers
