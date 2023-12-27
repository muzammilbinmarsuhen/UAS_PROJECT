from django.contrib import admin
from .models import Person,Jamil
# Register your models here.


class JamilAdmin(admin.ModelAdmin):
    list_display = ("Person", "pekerjaan", "status")


admin.site.register(Jamil, JamilAdmin)
admin.site.register(Person)
