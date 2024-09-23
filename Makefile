test:
	poetry run python manage.py test polls_test
start:
	poetry run python manage.py runserver
note:
	poetry run python manage.py shell_plus --notebook