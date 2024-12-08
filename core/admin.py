from django.contrib import admin
from .models import Usuario, Cliente, Endereco, Pet, Raca, Atendimento

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Pet)
admin.site.register(Raca)
admin.site.register(Atendimento)