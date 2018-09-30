from rest_framework import serializers
from .models import Bucketlist
from .models import Teste
from .models import Cliente, Notificacao, Promocao, Categoria, Prestador, Servico


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


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ("id", "nome", "cpf", "email", "data_nasc")

class NotificacaoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Notificacao
        fields = ("id", "descricao", "data", "hora")

class PromocaoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Promocao
        fields = ("id", "titulo", "descricao", "imagem", "data", "hora")



class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categoria
        fields = ("id", "nome")

class PrestadorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Prestador
        fields = ("id", "nome", "cpf", "email", "data_nasc")

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Servico
        fields = ("id", "titulo", "descricao", "valor", "imagem", "tipo", "data", "hora")