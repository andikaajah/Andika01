from django.contrib import admin
from .models import Produk
from .models import Katagori

# Register your models here.

admin.site.register(Produk)
admin.site.register(Katagori)