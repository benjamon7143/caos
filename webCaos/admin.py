from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Periodista)
admin.site.register(Categoria)
admin.site.register(Noticia)