test:
	poetry run python manage.py test polls
start:
	poetry run python manage.py runserver
note:
	poetry run python manage.py shell_plus --notebook