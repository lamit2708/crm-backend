# Upgrade Postgres Guidline

[REF](https://dba.stackexchange.com/questions/98144/how-to-upgrade-postgresql-from-version-8-4-to-9-4)
[REF](https://computingforgeeks.com/how-to-install-postgresql-12-on-centos-7/)

## Check centos version

## Check Linux Kernel version

    uname -a

## Check pg package

    rpm -qa | grep pgdg

## Config Network Access

nano /var/lib/pgsql/12/data/postgresql.conf

    listen_addresses = '*'
    port = 5432

nano /var/lib/pgsql/12/data/pg_hba.conf

    host all all 0.0.0.0/0 md5
    host all all ::/0 md5

## Update method md5

Maybe you actually want to connect with a password, not Ident. Edit the pg_hba.conf file appropriately. For example, change:

    host all all 127.0.0.1/32 ident

to

    host all all 127.0.0.1/32 md5

then
sudo systemctl restart postgresql-12

## Remove PG8.4

    yum remove postgresql
    ln -s /usr/pgsql-9.4/bin/psql /usr/local/bin/psql

## Add Repo for postgres

[REF](https://sysadminxpert.com/install-postgresql-12-on-centos-7-or-rhel-7/)

    yum install -y https://download.postgresql.org/pub/repos/yum/12/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

## Install postgres

    yum install postgresql12 postgresql12-server postgresql12-contrib postgresql12-libs -y

## Initialize PostgreSQL

    /usr/pgsql-12/bin/postgresql-12-setup initdb

## Start/Enable PostgreSQL

    systemctl enable postgresql-12.service

    systemctl start postgresql-12.service

## Check Postgres Service

    systemctl status postgresql-12.service

## Assign Environment Path on Centos

    sudo nano /etc/sudoers

modify the following text from:

    Defaults secure_path = /sbin:/bin:/usr/sbin:/usr/bin

to

    Defaults secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/pgsql-12/bin

## Print Environment

    printenv PATH

    sudo su postgres

    psql
