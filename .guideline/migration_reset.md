# Guide to reset Migrations

[REF](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

## Remove the all migrations files within your project

Go through each of your projects apps migration folder and remove everything inside, except the **init**.py file.

Or if you are using a unix-like OS you can run the following script (inside your project dir):

    find . -path "_/migrations/_.py" -not -name "**init**.py" -delete
    find . -path "_/migrations/_.pyc" -delete

## Drop the current database

## Create the initial migrations and generate the database schema

    python manage.py makemigrations
    python manage.py migrate

    And you are good to go.

    python manage.py showmigrations

    python manage.py migrate admin zero
    python manage.py migrate auth zero
    python manage.py migrate contenttypes zero
    python manage.py migrate sessions zero
