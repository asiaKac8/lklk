# Django Prediction App
## Getting Started
This application works on **Python 3+** \
Install dependencies:
```
pip install -r requirements.txt
```
Prepare database:
```
python manage.py makemigrations
python manage.py migrate
```
Run server locally:
```
python manage.py runserver
```

---
## Database

create superuser:
```
python manage.py createsuperuser
```

clear db:
```
python manage.py flush
```

migrate without errors
```
python manage.py migrate --fake
```
