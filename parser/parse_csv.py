import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from main.models import Event


def load_data_to_model(file_path):
    """Функция для парсинга CSV файла и загрузки данных в модель"""

    with open(file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        events = []

        for row in csv_reader:
            events.append(
                Event(
                    institution=row[1],
                    region=row[2],
                    address=row[3],
                    year=row[4],
                    budget_amount=row[5],
                )
            )
        Event.objects.bulk_create(events)


csv_file_path = "opendata.csv"
load_data_to_model(csv_file_path)
