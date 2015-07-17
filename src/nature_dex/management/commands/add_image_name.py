# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from nature_dex.models import Specimen

# That command saves in the field specimen_image, the str form by "images/" + scientific_name
# formated in a correct way

class Command(BaseCommand):
    args = ''
    help = 'Add image name'

    def handle(self, *args, **options):
        self.add_image_name()


    def add_image_name(self):
        specimenes = Specimen.objects.all()
        for s in specimenes:
            scientific_name = s.scientific_name.lower().replace(' ', '-').replace('/', '-')
            spec_photo = "images/{}.jpg".format(scientific_name)
            s.specimen_image = spec_photo
            s.save()
            print("{} saved".format(spec_photo))
