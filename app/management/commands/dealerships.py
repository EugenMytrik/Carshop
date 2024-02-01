from django.core.management.base import BaseCommand
from app.models import *


class Command(BaseCommand):
    help = "Generate some data"

    def handle(self, *args, **kwargs):
        cities = ["Dnipro", "Kyiv", "Odesa", "Kharkiv", "Lviv", "Kryvij Rih"]

        for i in cities:
            city = Dealership(name=i)
            city.save()
