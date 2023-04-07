# import os
# from django.contrib.auth import get_user_model
# from django.core.management import BaseCommand
# from common.models import City
# import csv
#
# from config.settings import BASE_DIR
#
# User = get_user_model()
#
#
# def csv_to_list(path):
#     data = []
#     with open(path, mode="r", encoding="utf8") as infile:
#         reader = csv.reader(infile)
#         z = 0
#         for row in reader:
#             if z == 0:
#                 header = row
#                 z = 1
#             else:
#                 temp = {}
#                 for i, n in enumerate(row):
#                     temp.update({header[i]: n})
#                 data.append(temp)
#     return data
#
#
# cities = csv_to_list(os.path.join(BASE_DIR, "common", "files", 'provinces.csv'))
#
#
# class Command(BaseCommand):
#     help = 'create city '
#
#     def add_arguments(self, parser):
#         parser.add_argument(
#             '--clear',
#             action='store_true',
#             help='clear old cities',
#         )
#
#     def handle(self, *args, **options):
#         if options['clear']:
#             City.objects.all().delete()
#             self.stdout.write(self.style.SUCCESS(f"CLEAR"))
#         for city in cities:
#             City.objects.get_or_create(
#                 id=city['id'],
#                 name=city['name']
#             )
#             self.stdout.write(self.style.SUCCESS(f"add {city['name']} city"))
