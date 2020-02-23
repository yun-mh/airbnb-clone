from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates superusers"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser(
                "ebadmin", "minhoyun.dev@gmail.com", "1q2w3e4r5"
            )
            self.stdout.write(self.style.SUCCESS("Superusers created"))
        else:
            self.stdout.write(self.style.SUCCESS("Superusers created"))

