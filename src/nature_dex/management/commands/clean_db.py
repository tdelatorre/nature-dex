# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from nature_dex.models import Specimen

import re

# That command clean the field identification in Specimen table

class Command(BaseCommand):
    args = ''
    help = 'Clean db'

    def handle(self, *args, **options):
        self.clean_db()


    def clean_db(self):
        specimenes = Specimen.objects.all()
        for s in specimenes:
            dirty_text = s.identification
            patter = re.compile('<sup.*?</sup>', re.I | re.S)
            patter2 = re.compile('<p>Ver texto</p>', re.I | re.S)
            patter3 = re.compile('<p>Se reconocen.*?<a target="blank" .*?>subespecies.*?:</p>', re.I | re.S)
            patter4 = re.compile('<p>Ver tecto.</p>', re.I | re.S)
            patter5 = re.compile('<p>Otras especies reconocidas por Nyffeler in Eggli 2004 son:</p><p>Una especie reciente:</p>', re.I | re.S)
            patter6 = re.compile('<p>Se conocen.*?<a target="blank" .*?>subespecies.*?:</p>', re.I | re.S)
            patter7 = re.compile('<p><span style="margin:0px; padding-bottom:1px; font-size:90%; display:block;"><span style="border: 1px solid; border: .*?; background-color:.*?; color:white">    </span> .*?</span></p>', re.I | re.S)
            patter8 = re.compile('<p>Mirar texto</p>', re.I | re.S)
            patter9 = re.compile('<p>Ver texto.</p>', re.I | re.S)
            patter10 = re.compile('<p>Véase el texto</p>', re.I | re.S)
            patter11 = re.compile('<p>Se reconocen las siguientes especies:</p>', re.I | re.S)
            patter12 = re.compile('<p><a target="blank" href="https://es.wikipedia.org/wiki/Gustav_M%C3%BCtzel" title="Gustav Mützel">Gustav Mützel</a>, para <a target="blank" href="https://es.wikipedia.org/wiki/Alfred_Brehm" title="Alfred Brehm">Alfred Brehm</a>. <a target="blank" class="mw-redirect" href="https://es.wikipedia.org/wiki/A%C3%B1o_1927" title="Año 1927">1927</a>.</p>', re.I | re.S)
            patter13 = re.compile('<p>Se reconocen.*?<a target="blank" .*?>subespecies.*?.</p>', re.I | re.S)
            patter14 = re.compile('<p>Se han identificado las siguientes subespecies:</p>', re.I | re.S)
            clean_text = patter.sub("", dirty_text)
            clean_text2 = patter2.sub("", clean_text)
            clean_text3 = patter3.sub("", clean_text2)
            clean_text4 = patter4.sub("", clean_text3)
            clean_text5 = patter5.sub("", clean_text4)
            clean_text6 = patter6.sub("", clean_text5)
            clean_text7 = patter7.sub("", clean_text6)
            clean_text8 = patter8.sub("", clean_text7)
            clean_text9 = patter9.sub("", clean_text8)
            clean_text10 = patter10.sub("", clean_text9)
            clean_text11 = patter11.sub("", clean_text10)
            clean_text12 = patter12.sub("", clean_text11)
            clean_text13 = patter13.sub("", clean_text12)
            clean_text14 = patter14.sub("", clean_text13)
            s.identification = clean_text14
            s.save()
            print("{} cleaned".format(s.common_name))
