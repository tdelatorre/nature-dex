# -*- coding: utf-8 -*-

from rest_framework import filters, exceptions
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


class SpecimenByZoneFilter(filters.BaseFilterBackend):
    # Example url with filter http://localhost:8000/specimenes/?lon=-3.6713546&lat=40.4360407
    # Example filter also with filter group http://localhost:8000/specimenes/?lon=-3.6713546&lat=40.4360407&group=Aves
    def filter_queryset(self, request, queryset, view):
        lat = request.QUERY_PARAMS.get('lat', None)
        lon = request.QUERY_PARAMS.get('lon', None)

        if lat or lon:
            try:
                lon = float(lon)
                lat = float(lat)
            except ValueError:
                raise exceptions.ParseError(detail=u'Incorrect point params')

            point = Point((lon, lat))
            queryset = queryset.filter(specimenbyzone__zone__mpoly__contains=point)

        return queryset

