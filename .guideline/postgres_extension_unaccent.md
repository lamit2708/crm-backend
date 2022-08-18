# Guileline for search a unaccent string

[REF](https://stackoverflow.com/questions/54071944/fielderror-unsupported-lookup-unaccent-for-charfield-or-join-on-the-field-not)
[REF](<https://github.com/cursame/cursame-rails/wiki/CREATE-EXTENSION-unaccent;-(PostgreSQL)>)

## Enable the unaccent extension on postgres

Switch to postgres user

    sudo su - postgres

Connect to the database

    \$ psql db_aznose

psql -h 112.213.86.173 -p 5432 -d db_aznose -U aznose -W
Create the extension

    CREATE EXTENSION unaccent;
    exit;
