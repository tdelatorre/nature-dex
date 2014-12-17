from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import DefaultRouter
from nature_dex.views import SpecimenViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'^specimenes', SpecimenViewSet, 'specimenes')
router.register(r'^groups', GroupViewSet, 'groups')
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nature.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(gisadmin.site.urls)),
    url(r'^file/', TemplateView.as_view(template_name='file.html'), name='file'),
    url(r'^listview/', TemplateView.as_view(template_name='listview.html'), name='file'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
)

def mediafiles_urlpatterns():
    """
    Method for serve media files with runserver.
    """

    _media_url = settings.MEDIA_URL
    if _media_url.startswith("/"):
        _media_url = _media_url[1:]

    from django.views.static import serve
    return [
        url(r"^%s(?P<path>.*)$" % _media_url, serve,
            {"document_root": settings.MEDIA_ROOT})
    ]


# Static & Media
urlpatterns += staticfiles_urlpatterns()
urlpatterns += mediafiles_urlpatterns()
