# Start Aznose Project

## Clone Repository

Jump to github
LINK <https://github.com/lamit2708/crm-backend> Example
Click Code> Copy
Visual Studio Code>Clone Git Repository> Past> OK> Select Repository Location

## Folder Frontend

/mnt/Data/aznose/src/AZNose/sources/admin-manage

## Frontend Setup have the error

### to update npm because it is sometimes buggy

npm install -g npm@latest

### to remove the existing modules

rm -rf node_modules

### to re-install the project dependencies

npm install
npm audit fix

## Folder Backend

/mnt/Data/aznose/src/AZNose/sources/aznose

## Seting Virtual Python Environment Backend

Create Virtual Environment env

```bash
python3 -m venv env
```

Use virtual environemnt

```bash
source ./env/bin/activate
```

Install requirements

```bash
#pip install -r requirements.txt
python3 -m pip install -r requirements.txt
```

## Start backend

source ./env/bin/activate
python3 manage.py runserver 127.0.0.1:8000

## Install Frontend

yarn install

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

[Local](http://127.0.0.1:8000/api/signup/)
{
"username": "admin321",
"email":"admin321",
"password":"0biet321"
}

## Setup with git

Click commit to update code to save in the local server
Click sync to update code to the git server
