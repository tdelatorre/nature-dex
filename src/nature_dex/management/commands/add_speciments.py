# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from nature_dex.models import Specimen, Zone, SpecimenByZone

from optparse import make_option
import csv

CSV_SETTINGS = {
    'delimiter': ',',
    'lineterminator': '"',
}

class Command(BaseCommand):
    args = ''
    help = 'Import speciments'
    #output_transaction = True
    option_list = BaseCommand.option_list + (
        make_option(
            "-f",
            "--file",
            dest = "file",
            help = "specify import file",
            metavar = "FILE"
        ),
    )

    def handle(self, *args, **options):
        # make sure file option is present
        if options['file'] is None:
            raise CommandError("Option `--file=...` must be specified.")

        self.import_sp(options['file'])


    def import_sp(self, import_file):
        with open(import_file, 'r') as csvfile:
            spreader = csv.DictReader(csvfile, **CSV_SETTINGS)
            for i, row in enumerate(spreader):
                try:
                    fields_for_sp = self.parse_fields(row)
                    if fields_for_sp:
                        specimen = Specimen.objects.filter(ext_ref=fields_for_sp['ext_ref'])
                        if not specimen[0]:
                            print(u'Creating speciment')
                            Specimen.objects.create(
                                ext_ref = fields_for_sp['ext_ref'],
                                scientific_name = fields_for_sp['scientific_name'],
                                group = fields_for_sp['group'],
                                genus = fields_for_sp['genus'],
                                species = fields_for_sp['species'],
                                kingdom = fields_for_sp['kingdom'],
                                division = fields_for_sp['division'],
                                kind = fields_for_sp['kind'],
                                order = fields_for_sp['order'],
                                family = fields_for_sp['family'],
                            )

                except Exception as ex:
                    print(u'**ERROR {}'.format(str(ex)))

                finally:
                    if fields_for_sp:
                        zone = Zone.objects.filter(ext_ref=fields_for_sp['ref_zone'])
                        specimen = Specimen.objects.filter(ext_ref=fields_for_sp['ext_ref'])

                        if zone[0] and specimen[0]:
                            print(u'Creating speciment by zone')
                            SpecimenByZone.objects.create(
                                specimen = specimen[0],
                                zone = zone[0],
                            )


    def parse_fields(self, row):
        fields_for_sp = {
            'ref_zone': row['CUTM10x10'],
            'ext_ref': row['IdEspecie'],
            'scientific_name': row['Nombre'],
            'group': row['Grupo'],
            'genus': row['Genero'],
            'species': row['Especie'],
            'kingdom': row['Reino'],
            'division': row['Division'],
            'kind': row['Clase'],
            'order': row['Orden'],
            'family': row['Familia'],
        }
        return fields_for_sp

