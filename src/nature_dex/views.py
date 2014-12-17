# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend
from rest_framework.response import Response

from nature_dex.models import Specimen
from nature_dex.serializers import SpecimenSerializer
from nature_dex.filters import SpecimenByZoneFilter


class SpecimenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specimen.objects.all()
    filter_backends = (
        DjangoFilterBackend, SpecimenByZoneFilter
    )
    serializer_class = SpecimenSerializer
    filter_fields = ('kingdom', 'group',)
    ordering = ('common_name',)

class GroupViewSet(viewsets.ViewSet):

    def list(self, request):
        group_list = Specimen.objects.all().values('kingdom', 'group').distinct()
        return Response(group_list)