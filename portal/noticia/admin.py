from django.contrib import admin

from .models import Noticia, Autor

admin.site.register(Noticia)
admin.site.register(Autor)