# DRE Tournament Registration API

## Setup
- Python 3.10+, pip
- Install: pip install django djangorestframework
- Run: python manage.py migrate && python manage.py runserver
- Test: python manage.py test

## Assumptions
- No auth, SQLite, UTC deadlines

## Tradeoffs
- No pagination, basic concurrency handling

## What I would improve
- JWT auth, email notifications, race condition fix
