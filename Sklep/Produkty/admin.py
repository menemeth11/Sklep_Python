from django.contrib import admin
from .models import Produkty, Producenci, Kategorie, Stan
# Register your models here.

admin.site.register(Produkty)
admin.site.register(Producenci)
admin.site.register(Kategorie)
admin.site.register(Stan)
