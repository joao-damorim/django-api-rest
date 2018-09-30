from django.db import models

# Create your models here.

from django.db import models


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Teste(models.Model):
    nome = models.CharField(max_length=255, blank=False, unique=True)
    descricao = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.nome)



class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, unique=True)
    cpf = models.CharField(max_length=255, blank=False, unique=True)
    email = models.CharField(max_length=255, blank=False, unique=True)
    data_nasc = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

class Notificacao(models.Model):
    descricao = models.CharField(max_length=255, blank=False, unique=True)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return "{}".format(self.descricao)

class Promocao(models.Model):
    titulo = models.CharField(max_length=255, blank=False, unique=True)
    descricao = models.CharField(max_length=255, blank=False, unique=True)
    imagem = models.CharField(max_length=255, blank=False, unique=True)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return "{}".format(self.titulo)

class Categoria(models.Model):
    nome = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

class Prestador(models.Model):
    nome = models.CharField(max_length=255, blank=False, unique=True)
    cpf = models.CharField(max_length=255, blank=False, unique=True)
    email = models.CharField(max_length=255, blank=False, unique=True)
    data_nasc = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

class Servico(models.Model):
    titulo = models.CharField(max_length=255, blank=False, unique=True)
    descricao = models.CharField(max_length=255, blank=False, unique=True)
    valor = models.CharField(max_length=255, blank=False, unique=True)
    imagem = models.CharField(max_length=255, blank=False, unique=True)
    tipo = models.CharField(max_length=255, blank=False, unique=True)
    data =  models.CharField(max_length=255, blank=False, unique=True)
    hora = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.titulo)

class ClienteNotificacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    notificacao = models.ForeignKey(Notificacao, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

class ClientePromocao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    promocao = models.ForeignKey(Promocao, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

class ClienteNotificacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    notificacao = models.ForeignKey(Notificacao, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

class ClienteCategoria(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class CategoriaPrestador(models.Model):
    cliente = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    data = models.DateField()

class PrestadorServico(models.Model):
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()