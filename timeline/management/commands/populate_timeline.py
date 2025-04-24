# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from timeline.models import TimeLine


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = 'C:/Users/Usuario/Dev/clase_django_2025/timeline/management/commands/disney_peliculas_fix.csv'
        with open(path, mode='r', encoding='utf-8') as file:
            # Lee línea por línea
            for line in file:
                # Divide cada línea por el delimitador ';'
                data = line.strip().split(';')
                print(data)
                timeline = TimeLine()
                timeline.year = int(data[0])
                timeline.name = data[1]
                timeline.description = data[2]
                timeline.save()