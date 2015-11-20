from django.contrib import admin

# Register your models here.
from rkWebApp.models import Novica, Files

class NovicaAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date')

class FilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'novica')

admin.site.register(Novica, NovicaAdmin)
admin.site.register(Files, FilesAdmin)