# Postgres Guidline

## VERSION

sudo -u postgres psql -c "SELECT version();"

## CONNECT

psql -h localhost -p 5432 -d db_aznose -U aznose -W

## LOG POSTGRESQL

sudo su postgres
psql

## LOG SQL COMMAND

sudo -u postgres psql
psql -U user_name -d database_name -h 127.0.0.1 -W

## EXIT PSQL

\q
CTRL +D

## CREATE ROLE PSQL

createrole -interactive

## Create user

sudo su - postgres -c "createuser aznose"
or
sudo -u postgres createuser -interactive

## CREATE USER PSQL

create user myuser with encrypted password 'mypass';

## GRANT SUPER USER PSQL

ALTER ROLE aznose SUPERUSER;

## GRANT ALL Privileges

grant all privileges on database mydb to myuser;

## CHANGE PASSWORD PSQL

ALTER USER user_name WITH PASSWORD 'new_password';

## CREATE DB

sudo su - postgres -c "createdb db_aznose"

## CREATE DB PSQL

create database db_aznose;

## CONNECT DB PSQL

psql -d db_aznose

## Kill session to drop database

SELECT
pg_terminate_backend(pid)
FROM
pg_stat_activity
WHERE
-- don't kill my own connection!
pid <> pg_backend_pid()
-- don't kill the connections to other databases
AND datname = 'db_aznose';

## DROP Database

drop database db_aznose;

## DROP DB IF EXIST PSQL

DROP DATABASE [IF EXISTS] database_name;

## ENABLE EXTENSION unaccent

CREATE EXTENSION unaccent;

## SET ENCODING

ALTER ROLE yourprojectuser SET client_encoding TO 'utf8';

## LIST ROLE

postgres=# \du

## CREATE ROLE

CREATE ROLE demo_role;

## ASSIGN LOGIN

ALTER ROLE demo_role WITH LOGIN;

## GRANT ALL PRIV ON TABLE

GRANT ALL PRIVILEGES ON kinds TO manuel;
