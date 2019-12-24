# palimpsest
django + redis


## setup

Install dependencies using `pipenv` or you environment management tool of choice.

```bash
$ pipenv install -e .
```

Set up a database of choice (not covered - example uses PostgreSQL 11) and apply migrations in Django.

```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```


## usage

