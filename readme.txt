# creating the virtula environment

1.python3 -m venv myvenv
2.source myvenv/bin/activate

3.(myvenv) ~$ python -m pip install --upgrade pip

#Installing packages with requirements

djangogirls
└───requirements.txt

In your djangogirls/requirements.txt file you should add the following text:

djangogirls/requirements.txt
Django~=2.0.6
Now, run pip install -r requirements.txt to install Django.


# creating the first project

(myvenv) ~/djangogirls$ django-admin startproject mysite .


django-admin.py is a script that will create the directories and files for you. You should now have a directory structure which looks like this:

djangogirls
├───manage.py
├───mysite
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
└───requirements.txt


# changing setting

--> time zone
--> language code
--> statics

# creating the application

--> (myvenv) ~/djangogirls$ python manage.py startapp blog

--->
djangogirls
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt

--> go to models --> INSTALLED APP :
	add 'blog',


# creating blog post models

# creating table for model in database

---> (myvenv) ~/djangogirls$ python manage.py makemigrations blog

--> (myvenv) ~/djangogirls$ python manage.py migrate blog

# create django admin

To log in, you need to create a superuser - a user account that has control over everything on the site. Go back to the command line, type python manage.py createsuperuser, and press enter.

Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.


# to run the code

python manage.py runserver




# django models


# creating application

python manage.py startapp blog

# creating table for model in database

python manage.py makemigrations blog