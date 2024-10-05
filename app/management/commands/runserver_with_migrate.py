from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs migrations and starts the Django development server"

    def add_arguments(self, parser):
        # Allow any extra arguments like host and port
        parser.add_argument(
            "addrport",
            nargs="?",
            help="Optional address:port pair (default: 127.0.0.1:8000)",
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Making migrations..."))
        call_command("makemigrations")

        self.stdout.write(self.style.SUCCESS("Applying migrations..."))
        call_command("migrate")

        self.stdout.write(self.style.SUCCESS("Starting the development server..."))
        # Pass the optional address and port to runserver
        addrport = options.get("addrport") or "127.0.0.1:8000"
        call_command("runserver", addrport)
