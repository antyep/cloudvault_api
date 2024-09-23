from django.core.management.base import BaseCommand
from django_seed import Seed
from api.models import CustomUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Seed the database with unique usesrs."

    def handle(self, *arg, **kwargs):
        seeder = Seed.seeder()

        seeder.add_entity(CustomUser, 4000, {
            'email': lambda x: seeder.faker.unique.email(),
            'username': lambda x: seeder.faker.user_name(),
            'password': lambda x: make_password('defaultpassword'),
            'created_at': lambda x: timezone.now(),
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            'Users are successfully created. 👶🌱'))
