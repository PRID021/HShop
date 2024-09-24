# Define environment variables
DJANGO_ENV ?= dev
POETRY = poetry
PYTHON = $(POETRY) run python
app ?= polls

# Run the Django development server
runserver:
	$(POETRY) run python manage.py runserver

# Migrate database changes
migrate:
	$(POETRY) run python manage.py migrate --database=$(app)_db

# Make migrations
migrations:
	$(POETRY) run python manage.py makemigrations  $(app)

# Install dependencies
install:
	$(POETRY) install

# Run tests
test:
	$(POETRY) run python manage.py test $(app)/tests

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

# Open Django template dir
where_template:
	$(PYTHON) -c "import django; print(django.__path__)"