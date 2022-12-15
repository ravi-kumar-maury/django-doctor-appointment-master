# django-doctor-appointment-project


Please run below commands to start django Server:

### cd ~/django-doctor-appointment-master
### pip install -r requirements.txt
### python3 manage.py makemigrations
### python3 manage.py migrate
### python3 manage.py runserver

check the running server at : http://127.0.0.1:8000/

create a superuser which will able to acess /admin route

### python3 manage.py createsuperuser

## Features
1. anyone can check available doctor's either by location or department on home page
2. patient after registering can book an appointment and check their booked appointments or delete it.
3. doctors after registering can check the patients list and also can create their appointment for patients.
4. admin user can edit , update,delete all data
