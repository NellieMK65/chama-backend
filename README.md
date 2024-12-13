## Migrations

-   To setup migrations, run `alembic init migrations`. Run this command only once
-   Modify alembic.ini file and set the `sqlalchemy.url = sqlite:///chama.db`
-   Modify `env.py` and import the Base class from the models file and update the target_metadata
