# Guideline to manage your migrations

[REF](https://stackoverflow.com/questions/29253399/how-to-reset-migrations-in-django-1-7)

## Create migration after editing models

python manage.py makemigrations

## Update from migration to database

python manage.py migrate

## To do

Run

python manage.py migrate your_app zero

This will drop all tables from your_app

If you want, since you said you want to start over, you can delete your migrations folder, or maybe rename the folder, create a new migrations folder and run

python manage.py makemigrations your_app
python manage.py migrate your_app

Just like south, you can always go back and forth...

## 'Go to the first migration'

python manage.py migrate your_app 0001

## 'Go to the third migration'

python manage.py migrate your_app 0003

So imagine that your 4th migration is a mess... you can always migrate to the 3rd, remove the 4th migration file and do it again.

## Jump migration to zeror or number in django_migrations

Delete migrations and run the follow command

```bash
python manage.py migrate --fake tutorials zero
```

## Jump to the target migration 0001

```bash
python manage.py migrate tutorials 0001
```

Delete the migrations come after 0001
