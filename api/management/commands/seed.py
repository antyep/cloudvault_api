from django.core.management.base import BaseCommand
from django_seed import Seed
from api.models import CustomUser, Media
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def get_current_time(self):
        return timezone.now()

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        seeder.add_entity(CustomUser, 500, {
            'email': lambda x: seeder.faker.email(),
            'created_at': lambda x: timezone.now(),

        })

        inserted_pks = seeder.execute()

        users = list(CustomUser.objects.all())

        seeder.add_entity(Media, 4000, {
            'title': lambda x: seeder.faker.sentence(),
            'description': lambda x: seeder.faker.text(),
            'media_file': lambda x: 'media/testfile.jpg',
            'file_type': lambda x: random.choice(['image/jpeg', 'video/mp4']),
            'file_size': lambda x: random.randint(50, 20000),
            'user': lambda x: random.choice(users),
            'created_at': lambda x: timezone.now(),
            'is_public': lambda x: seeder.faker.boolean(),
            'is_deleted': lambda x: False,
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database'))
