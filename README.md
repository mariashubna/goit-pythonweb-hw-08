poetry env activate
poetry run alembic revision --autogenerate -m "Initial migration"
poetry run alembic upgrade head
