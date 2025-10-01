from django.contrib import admin
from app.models import *

admin.site.register(Autores)
admin.site.register(Genero)
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Leitor)
admin.site.register(Emprestimo)

# Register your models here.
