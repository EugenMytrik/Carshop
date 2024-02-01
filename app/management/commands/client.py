from django.core.management.base import BaseCommand
from faker import Faker
from app.models import *


class Command(BaseCommand):
    help = "Generate some data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, nargs="?", default=5)

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        fake = Faker()

        for i in range(count):
            client = Client(
                name=fake.first_name(), email=fake.email(), phone=fake.phone_number()
            )
            client.save()
