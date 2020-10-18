LimeHome Places test backend

# Run local

Python virtual env (using virtualenvwrapper)

`mkvirtualenv limehometest`

Create a database (using psql)

`create database limehometest`

Create settings_local

```
cd limehometest
touch settings_local.py
```

Populate it with secrets and set DEBUG

```
DEBUG = True

SECRET_KEY = 'your secret key'
HERE_API_KEY = 'your api key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'limehometest',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
```
Apply migrations

`python manage.py migrate`

Run server

`python manage.py runserver`
