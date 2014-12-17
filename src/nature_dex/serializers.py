from rest_framework import serializers
from nature_dex.models import Specimen

class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specimen

