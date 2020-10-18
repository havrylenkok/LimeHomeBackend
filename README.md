LimeHome Places test backend

Spec https://gitlab.com/limehome/interviews/full-stack-challenge/

Deploy https://limehometest-back.herokuapp.com/docs/

Docs https://limehometest-back.herokuapp.com/docs/

# Run locally


Create a Python virtual env (using virtualenvwrapper):

`mkvirtualenv limehometest`

Create a database (using PostgreSQL i.e. psql):

`create database limehometest`

Create settings_local:

```
cd limehometest
touch settings_local.py
```

Open it in an editor of your preference, populate it with secrets and set DEBUG:

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
Apply migrations to the database:

`python manage.py migrate`

Finally run server:

`python manage.py runserver`
