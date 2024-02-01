from django.core.management.base import BaseCommand
from app.models import *
from random import randint


class Command(BaseCommand):
    help = "Generate some data"

    def handle(self, *args, **kwargs):
        dnipro = Dealership.objects.get(pk=1)
        kyiv = Dealership.objects.get(pk=2)
        data1 = {
            "Mazda CX-5": "Mazda",
            "BMW X5": "BMW",
            "Mitsubishi Outlander": "Mitsubishi",
        }
        data2 = {
            "Kia Sportage": "Kia",
            "Audi Q5": "Audi",
            "Volkswagen Crozz ID4": "Volkswagen",
        }

        for name, brand in data1.items():
            car_type = CarType(
                name=name,
                brand=brand,
                price=randint(20000, 100000),
            )
            car_type.save()
            dnipro.available_car_types.add(car_type)

        for name, brand in data2.items():
            car_type = CarType(
                name=name,
                brand=brand,
                price=randint(20000, 100000),
            )
            car_type.save()
            kyiv.available_car_types.add(car_type)
