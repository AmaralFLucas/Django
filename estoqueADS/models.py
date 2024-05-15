from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255, default=None)

    def __str__(self) -> str:
        return self.nome

class Produtos(models.Model):
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, blank=True)
    imagem = models.ImageField(blank=True)
    preço = models.DecimalField(decimal_places=2, max_digits=9)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    codigo = models.CharField(max_length=12)
    em_estoque = models.BooleanField()
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"