from django.db import models

class Ficha(models.Model):
    nome_personagem = models.CharField(max_length=100)
    nome_jogador = models.CharField(max_length=100)
    
    forca = models.IntegerField()
    destreza = models.IntegerField()
    constituicao = models.IntegerField()
    inteligencia = models.IntegerField()
    sabedoria = models.IntegerField()
    carisma = models.IntegerField()
    
    pontos_vida = models.IntegerField()
    pontos_mana = models.IntegerField()
    defesa = models.IntegerField()

    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.nome_personagem} ({self.nome_jogador})\n"
                f"PV: {self.pontos_vida} | PM: {self.pontos_mana}"
                f"Classe: {self.classe} \n Raça: {self.raca}")
                