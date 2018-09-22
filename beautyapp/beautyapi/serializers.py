from rest_framework import serializers
from .models import Bucketlist
from .models import Teste


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class TesteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teste
        fields = ("id", "nome", "descricao")