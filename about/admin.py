from django.contrib import admin
from .models import Induk, Anak
# Register your models here.

class AnakAdmin(admin.ModelAdmin):
    list_display = ('jenis', 'status', 'umur',)


admin.site.register(Anak, AnakAdmin)
admin.site.register(Induk)


