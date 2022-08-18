import pgconnection
ALLOWED_HOSTS = ['localhost', '127.0.0.1','112.213.86.173','vegunsoft.vn']
DATABASES = pgconnection.configure({
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_aznose',
        'USER': 'aznose',
        'PASSWORD': 'aznose',
        'HOST': 'localhost',
        'PORT': '5432',
    }
})
