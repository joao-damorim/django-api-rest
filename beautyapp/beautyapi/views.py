from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import BucketlistSerializer
from .serializers import TesteSerializer
from .serializers import ClienteSerializer, CategoriaSerializer, PromocaoSerializer
from .models import Bucketlist
from .models import Teste
from .models import Cliente, Categoria, Promocao

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

class CreateViewTeste(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewTeste(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Teste.objects.all()
    serializer_class = TesteSerializer

class CreateViewCliente(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewCliente(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CreateViewPromocao(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewPromocao(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

class CreateViewCategoria(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewCategoria(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
