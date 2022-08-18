# Start Aznose Project

## Folder Frontend

/mnt/Data/aznose/src/AZNose/sources/admin-manage

## Folder Backend

/mnt/Data/aznose/src/AZNose/sources/aznose

## Start backend

source ./env/bin/activate
python3 manage.py runserver 127.0.0.1:8000

## Start frontend

yarn start

## Start Database Postgres

start pgadmin4
master password: 0biet
Choose My Local Database

## Login Admin page with super user

<http://127.0.0.1:8000/admin/>
user:admin; password:admin123
This is user from Database:db_aznose> Table:auth_user

## Frontend folder

/mnt/Data/aznose/src/AZNose/sources/admin-manage

## Backend folder

/mnt/Data/aznose/src/AZNose/sources/aznose

## Check API with Postman

http://127.0.0.1:8000/api/signup/
{
"username": "admin321",
"email":"admin321",
"password":"0biet321"
}
