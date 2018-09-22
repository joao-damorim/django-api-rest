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