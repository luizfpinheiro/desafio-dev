from django.db import models


class TipoTransacao(models.Model):
    descricao = models.CharField(max_length=50)
    bo_entrada = models.BooleanField(blank=True, null=True)
    sinal = models.CharField(max_length=1)

class Transacao(models.Model):
    tipo = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE)
    dt_cadastro = models.DateTimeField(auto_now=True)
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    nome_representante = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)
