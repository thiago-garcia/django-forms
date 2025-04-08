from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=64)
    email = models.EmailField()
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    hobbies = models.JSONField()
