poetry env activate
poetry run alembic revision --autogenerate -m "Initial migrations"
poetry run alembic upgrade head
