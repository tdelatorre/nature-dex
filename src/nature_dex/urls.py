from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.gis import admin as gisadmin

from rest_framework.routers import DefaultRouter
from nature_dex.views import SpecimenViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'^specimenes', SpecimenViewSet, 'specimenes')
router.register(r'^groups', GroupViewSet, 'groups')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nature.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(gisadmin.site.urls)),
)
