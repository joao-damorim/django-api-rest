from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import BucketlistSerializer
from .serializers import TesteSerializer
from .serializers import ClienteSerializer
from .models import Bucketlist
from .models import Teste
from .models import Cliente


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