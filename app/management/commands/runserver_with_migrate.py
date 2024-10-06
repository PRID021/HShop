import os

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection


def load_sql_script():
    # Determine the environment and set the script path accordingly
    if os.getenv("DJANGO_ENV") == "production":
        path = "path/to/your/prod_script.sql"
    elif os.getenv("DJANGO_ENV") == "test":
        path = "path/to/your/test_script.sql"
    else:
        path = "scripts/dev_script.sql"

    # Read and execute the SQL script
    if os.path.exists(path):
        with open(path, "r") as sql_file:
            sql_content = sql_file.read()

        # Use connection.cursor() to execute the raw SQL
        with connection.cursor() as cursor:
            cursor.execute(sql_content)
    else:
        raise FileNotFoundError(f"SQL script not found: {path}")


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

        if not os.getenv("LOAD_SCRIPTED"):
            try:
                self.stdout.write(self.style.SUCCESS("Loading SQL script..."))
                load_sql_script()  # Load the SQL script
                os.environ["LOAD_SCRIPTED"] = (
                    "True"  # Use string for environment variable
                )
                self.stdout.write(self.style.SUCCESS("SQL script loaded successfully!"))
            except FileNotFoundError as e:
                self.stdout.write(self.style.ERROR(f"FileNotFoundError: {str(e)}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))

        self.stdout.write(self.style.SUCCESS("Starting the development server..."))
        # Pass the optional address and port to runserver
        addrport = options.get("addrport") or "127.0.0.1:8000"
        call_command("runserver", addrport)
