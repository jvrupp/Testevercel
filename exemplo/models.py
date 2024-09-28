from django.db import models

# Create your models here.



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class Endereco(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.rua