from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import *

class SpecimenAdmin(admin.ModelAdmin):
    search_fields = ('scientific_name', 'common_name')
    list_filter = ('kingdom', 'group')

admin.site.register(Zone, gisadmin.GeoModelAdmin)
admin.site.register(Specimen, SpecimenAdmin)
admin.site.register(SpecimenByZone)
