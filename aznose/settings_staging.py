#SECRET_KEY = os.environ['SECRET_KEY']
import pgconnection
ALLOWED_HOSTS = ['198.211.99.20', 'localhost', '127.0.0.1', 'vegunsoft.vn']
DATABASES = pgconnection.configure({
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_aznose',
        'USER': 'aznose',
        'PASSWORD': 'aznose',
        'HOST': '112.213.86.173',
        'PORT': '5432',
    }
})
