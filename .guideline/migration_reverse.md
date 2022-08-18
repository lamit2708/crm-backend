# Guideline to reverse a migration

## Reverse the last migration

[REF](https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration)

You can revert by migrating to the previous migration.

For example, if your last two migrations are:

1. 0010_previous_migration
2. 0011_migration_to_revert

Then you would do:

./manage.py migrate my_app 0010_previous_migration

You can then delete migration 0011_migration_to_revert.

## show the names of all the migrations with

./manage.py showmigrations my_app

## To reverse all migrations for an app, you can run

./manage.py migrate my_app zero

## Reverse manually, used this when you created a migration but did not run "./manage.py migrate " yet

```bash
rm myapp/migrations/0011*
```

Logged into database and ran this SQL (postgres in this example)

```sql
delete from django_migrations where name like '0011%';
```

I was then able to create new migrations that started with the migration number that I had just deleted (in this case, 11).

## Revert fake migration and delete table manually

If the last migration is (are) not easily revertible then it is possible to cautiously (after database backup) do a fake revert ./manage.py migrate --fake my_app 0010_previous_migration, delete the table manually.

If necessary, create a fixed migration from the fixed model and apply it without changing the database structure ./manage.py migrate --fake my_app 0011_fixed_migration.
