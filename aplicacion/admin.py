from django.contrib import admin
from .models import Cliente, Juguete, Ropa, Hogar

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Juguete)
admin.site.register(Ropa)
admin.site.register(Hogar)