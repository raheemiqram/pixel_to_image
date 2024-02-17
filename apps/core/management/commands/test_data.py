from django.core.management import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create Admin Account
        User.objects.create_user(
            email="admin@admin.com",
            password="admin@admin.com",
            is_superuser=True,
            is_staff=True,
            first_name="Abdur",
            last_name="Raheem",
        )
        print("Test data loaded successfully")
