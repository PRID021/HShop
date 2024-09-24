# Define environment variables
DJANGO_ENV ?= dev
POETRY = poetry
PYTHON = $(POETRY) run python

# Run the Django development server
runserver:
	$(POETRY) run python manage.py runserver

# Migrate database changes
migrate:
	$(POETRY) run python manage.py migrate

# Make migrations
makemigrations:
	$(POETRY) run python manage.py makemigrations

# Install dependencies
install:
	$(POETRY) install

# Run tests
test:
	$(POETRY) run python manage.py test polls/tests

# Run the server with environment variables
serve:
	DJANGO_ENV=$(DJANGO_ENV) $(PYTHON) manage.py runserver

# Create a superuser
createsuperuser:
	$(POETRY) run python manage.py createsuperuser

# Collect static files
collectstatic:
	$(POETRY) run python manage.py collectstatic --noinput

# Clean up pyc files
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Enter the Poetry shell
shell:
	$(POETRY) shell

# Example usage: 'make runserver' will run the Django server.

# Start jupyter sever, convience for testing.
jupyter:
	$(PYTHON) manage.py shell_plus --notebook