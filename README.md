## Migrations

-   To setup migrations, run `alembic init migrations`. Run this command only once
-   Modify alembic.ini file and set the `sqlalchemy.url = sqlite:///chama.db`
-   Modify `env.py` and import the Base class from the models file and update the target_metadata
-   To create a migration, run `alembic revision --autogenerate -m "message"`
-   To apply the generate migration, run `alembic upgrade head`
