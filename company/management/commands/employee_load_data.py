from django.core.management.base import BaseCommand
from company.models import Employee
import csv
import sys

csv.field_size_limit(sys.maxsize)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        file_path = options['path']
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                Employee.objects.create(**_object_dict)
