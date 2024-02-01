from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from app.models import CarType, Car


class Command(BaseCommand):
    help = "Generates the cars"

    def handle(self, *args, **options):
        fake = Faker()

        Car.objects.create(
            car_type=CarType(id=1), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=2), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=2), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=2), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=3), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=3), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=6), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=4), color=fake.color(), year=randint(2010, 2023)
        )
        Car.objects.create(
            car_type=CarType(id=5), color=fake.color(), year=randint(2010, 2023)
        )
