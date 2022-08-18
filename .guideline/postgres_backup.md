# Backup And Restore Guidline

    [REF](http://webfaver.com/database/huong-dan-backup-va-restore-postgres-database.html)

## Backup Data

    su - postgres

    pg_dumpall > dump.sql

## Restore Data

    service postgresql stop

    service postgresql-9.4 start

    su - postgres

    psql < dump.sql

## Remote Backup Data

    pg_dump -U aznose -h 112.213.86.173 -W -a -d db_aznose -f db_aznose_backup.sql

## Remote Backup Schema

    pg_dump -U aznose -h 112.213.86.173 -W -s -d db_aznose -f db_aznose_backup.sql

## Remote Restore Data

    psql -U john -h localhost -W -d mydb -1 -f backup.sql

## Backup with the compress file

    pg_dump -U aznose -h 112.213.86.173 -W -a -d db_aznose -Fc -Z5 -f db_aznose_z5.psql

## Retore with the compress file

    pg_restore -U john -h localhost -W -j 8 -d mydb backup.psql
