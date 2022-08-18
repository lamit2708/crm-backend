# AZNose Project

## Getting Started

Create project crm

```bash
django-admin startproject crm
```

Run server

```bash
python manage.py runserver
```

Create app

```bash
python manage.py startapp accounts
```

Create file accounts/urls.py
Create superuser

### Seting Virtual Python Environment

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

### Manage packages by pip in the backend environment

Ignore virtual environment from git

```bash
echo ‘env' > .gitignore
```

Create requirements

```bash
pip freeze > requirements.txt
```

Add requirements to git

```bash
git add requirements.txt
```

### Prerequisites

### Installing

Install requirements

```bash
#pip install -r requirements.txt
```

## Running the tests

```bash
python3 manage.py runserver
```

access link /api/[model_name]
[model_name] defined in /sources/aznose/urls.py
example: <http://127.0.0.1:8000/api/customer/>

### Break down into end to end tests

Explain what these tests test and why

### And coding style tests

Explain what these tests test and why

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Reactjs](https://reactjs.org/) - The web frontend
- [Django Rest Framework](https://www.django-rest-framework.org/) - The backend
- [PostgreSQL](https://www.postgresql.org/) - Database

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Le Vu Lam** - _Initial work_ - [AZNose](https://github.com/mac7285/AZNose)
- **Dang The Nhan**
- **Phat**

## License

This project is licensed under the Aznose Team

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
