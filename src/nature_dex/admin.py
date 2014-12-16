from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import *


admin.site.register(Zone, gisadmin.GeoModelAdmin)
admin.site.register(Specimen)
admin.site.register(SpecimenByZone)
