from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
     nome_autor = models.CharField(max_length=255)
     email_autor = models.EmailField ( null= True, blank =True )

     def __str__(self):
        return self.nome_autor

        class Meta:
            Verbose_name_plural("Autores")


# class Livros (models.Model):
#     titulo = models.CharField (max_length = 255)
#     isbn = models.CharField (max_length = 32, null = True, blank = True)
#     qtd = models.IntegerField (default = 0, null = True, blank = True)
#     preco = models.DecimalField (max_digits=7, decimal_places=2, default=0, null=True, blank=True)

#     def __str__(self):
#         return f"{self.titulo} ({self.qtd})"