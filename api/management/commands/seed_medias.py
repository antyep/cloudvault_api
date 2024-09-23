from django.core.management.base import BaseCommand
from django_seed import Seed
from api.models import Media, CustomUser
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Seed the database with media'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        users = CustomUser.objects.all()

        seeder.add_entity(Media, 6000, {
            'title': lambda x: seeder.faker.sentence(),
            'description': lambda x: seeder.faker.text(),
            'media_file': lambda x: f'media/testfile_{x}.jpg',
            'file_type': lambda x: random.choice(['image/jpeg', 'video/mp4']),
            'file_size': lambda x: random.randint(50, 20000),
            'user': lambda x: random.choice(users),
            'created_at': lambda x: timezone.now(),
            'is_public': lambda x: seeder.faker.boolean(),
            'is_deleted': lambda x: False,
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            'Medias are successfully created. 🎥🌱'))
