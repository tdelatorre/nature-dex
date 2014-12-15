from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.translation import ugettext_lazy as _

class Zone(models.Model):
    ext_ref = models.CharField(
        max_length=10, null=False, editable=False,
        unique=True,
        verbose_name=_(u'External reference')
    )
    marine = models.BooleanField(
        blank=False, null=False,
        default=False,
        verbose_name=_(u'Marine')
    )
    mpoly = models.MultiPolygonField()
    objects = gismodels.GeoManager()

    class Meta:
        verbose_name = _(u'Zone')
        verbose_name_plural = _(u'Zones')

    def __unicode__(self):
        return _(u'zone "{}"').format(self.ext_ref)


class Specimen(models.Model):
    ext_ref = models.CharField(
        max_length=50, null=False, editable=False,
        unique=True,
        verbose_name=_(u'External reference')
    )
    common_name = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Scientific name')
    )
    scientific_name = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Scientific name')
    )
    group = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Group')
    )
    genus = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Genus')
    )
    species = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Species')
    )
    kingdom = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Kingdom')
    )
    division = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Division')
    )
    kind = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Kind (Class)')
    )
    order = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Order')
    )
    family = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Family')
    )

    class Meta:
        verbose_name = _(u'Specimen')
        verbose_name_plural = _(u'Specimenes')

    def __unicode__(self):
        return _(u'specimen "{}"').format(self.scientific_name)


