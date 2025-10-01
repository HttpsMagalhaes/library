from django.db import models
   
class Genero(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Gênero")

    def __str__(self):
        return f'{self.nome}'
    
    class Meta:
        verbose_name = "Gênero" 
        verbose_name_plural = "Gêneros"

class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=50, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta: 
        verbose_name = "Cidade" 
        verbose_name_plural = "Cidades"
    
class Autores(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do autor")
    site = models.CharField(max_length=50, verbose_name="Site do autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do autor")

    def __str__(self):
        return f'{self.nome}'
    
    class Meta: 
        verbose_name = "Autor" 
        verbose_name_plural = "Autores"
    
class Editora(models.Model):
    nome = models.CharField(max_length=500, verbose_name="Nome da editora")
    site = models.CharField(max_length=50, verbose_name="Site da editora")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da editora")

    def __str__(self):
        return f'{self.nome}'
    
    class Meta: 
        verbose_name = "Editora" 
        verbose_name_plural = "Editoras"
    
class Livro(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do livro")
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, verbose_name="Autor do livro")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço do livro")
    data_publicacao = models.DateField(verbose_name="Data de publicação do livro")
    status = models.BooleanField(verbose_name="Status do livro")

    def __str__(self):
        return f'{self.nome, self.autor, self.editora, self.genero, self.preco, self.data_publicacao, self.status}'
    
    class Meta: 
        verbose_name = "Livro" 
        verbose_name_plural = "Livros"

class Leitor(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do leitor")
    email = models.CharField(max_length=100, verbose_name="Email do leitor")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")

    def __str__(self):
        return f'{self.nome}'
        
    
    class Meta: 
        verbose_name = "Leitor" 
        verbose_name_plural = "Leitores"

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.data_emprestimo, self.data_devolucao, self.leitor, self.livro}'
# Create your models here.
