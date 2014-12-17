from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.translation import ugettext_lazy as _

class Zone(gismodels.Model):
    ext_ref = models.CharField(
        max_length=10, null=False,
        unique=True,
        verbose_name=_(u'External reference')
    )
    marine = models.BooleanField(
        blank=False, null=False,
        default=False,
        verbose_name=_(u'Marine')
    )
    mpoly = gismodels.MultiPolygonField()
    objects = gismodels.GeoManager()

    class Meta:
        verbose_name = _(u'Zone')
        verbose_name_plural = _(u'Zones')

    def __unicode__(self):
        return _(u'zone "{}"').format(self.ext_ref)

    def __str__(self):
        return _(u'{}').format(self.ext_ref)


class Specimen(models.Model):
    ext_ref = models.CharField(
        max_length=50, null=False,
        unique=True,
        verbose_name=_(u'External reference')
    )
    specimen_image = models.ImageField(
        null=True, blank=True,
        default=None, upload_to='images'
    )
    track_image = models.ImageField(
        null=True, blank=True,
        default=None, upload_to='images'
    )
    leaf_image = models.ImageField(
        null=True, blank=True,
        default=None, upload_to='images'
    )
    common_name = models.CharField(
        max_length=255, blank=True, null=False,
        verbose_name=_(u'Common name')
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
    identification = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Identification')
    )
    status = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Status')
    )
    distribution = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Distribution')
    )
    habitat = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Habitat')
    )
    diet = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Diet')
    )
    reproduction = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Reproduction')
    )
    interactions = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Interactions')
    )
    behavior = models.TextField(
        blank=True, null=False,
        verbose_name=_(u'Behavior')
    )

    class Meta:
        verbose_name = _(u'Specimen')
        verbose_name_plural = _(u'Specimenes')

    def __unicode__(self):
        return _(u'specimen "{}"').format(self.scientific_name)

    def __str__(self):
        return _(u'{}').format(self.scientific_name)


class SpecimenByZone(models.Model):
    specimen = models.ForeignKey(
        'Specimen', blank=False, null=False,
        verbose_name=_(u'Specimen')
    )
    zone = models.ForeignKey(
        'Zone', blank=False, null=False,
        verbose_name=_(u'Zone')
    )

    class Meta:
        verbose_name = _(u'Specimen by zone')
        verbose_name_plural = _(u'Specimenes by zones')

    def __unicode__(self):
        return _(u'specimen "{}" by zone "{}"').format(self.specimen, self.zone)

    def __str__(self):
        return _(u'specimen "{}" by zone "{}"').format(self.specimen, self.zone)

