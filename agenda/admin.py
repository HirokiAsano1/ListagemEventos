from django.contrib import admin
from agenda.models import Evento
from agenda.models import Categoria
# Register your models here.

admin.site.register(Evento)
admin.site.register(Categoria)