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


--> manage.py is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

--> The settings.py file contains the configuration of your website.



# changing setting

mysite/settings.py
TIME_ZONE = 'Europe/Berlin'


mysite/settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


mysite/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

--> time zone
--> language code
--> statics


#Set up a database


Set up a database
There's a lot of different database software that can store data for your site. We'll use the default one, sqlite3.

This is already set up in this part of your mysite/settings.py file:

mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

(myvenv) ~/djangogirls$ python manage.py migrate

#Starting the web server

(myvenv) ~/djangogirls$ python manage.py runserver

#Django models

What we want to create now is something that will store all the posts in our blog. But to be able to do that we need to talk a little bit about things called objects.

Objects
There is a concept in programming called object-oriented programming. The idea is that instead of writing everything as a boring sequence of programming instructions, we can model things and define how they interact with each other.

So what is an object? It is a collection of properties and actions. It sounds weird, but we will give you an example.

If we want to model a cat, we will create an object Cat that has some properties such as color, age, mood (like good, bad, or sleepy ;)), and owner (which could be assigned a Person object – or maybe, in case of a stray cat, this property could be empty).

Then the Cat has some actions: purr, scratch, or feed (in which case, we will give the cat some CatFood, which could be a separate object with properties, like taste).

Cat
--------
color
age
mood
owner
purr()
scratch()
feed(cat_food)
CatFood
--------
taste
So basically the idea is to describe real things in code with properties (called object properties) and actions (called methods).

How will we model blog posts then? We want to build a blog, right?

We need to answer the question: What is a blog post? What properties should it have?

Well, for sure our blog post needs some text with its content and a title, right? It would be also nice to know who wrote it – so we need an author. Finally, we want to know when the post was created and published.

Post
--------
title
text
author
created_date
published_date
What kind of things could be done with a blog post? It would be nice to have some method that publishes the post, right?

So we will need a publish method.

Since we already know what we want to achieve, let's start modeling it in Django!

Django model
Knowing what an object is, we can create a Django model for our blog post.

A model in Django is a special kind of object – it is saved in the database. A database is a collection of data. This is a place in which you will store information about users, your blog posts, etc. We will be using a SQLite database to store our data. This is the default Django database adapter – it'll be enough for us right now.

You can think of a model in the database as a spreadsheet with columns (fields) and rows (data).





# creating the application


o keep everything tidy, we will create a separate application inside our project. 
It is very nice to have everything organized from the very beginning. 
To create an application we need to run the following command in the console (from djangogirls directory where manage.py file is):



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

In the blog/models.py file we define all objects called Models – this is a place in which we will define our blog post.

Let's open blog/models.py in the code editor, remove everything from it, and write code like this:

blog/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone


# creating table for model in database

---> (myvenv) ~/djangogirls$ python manage.py makemigrations blog

--> (myvenv) ~/djangogirls$ python manage.py migrate blog

# create django admin

To log in, you need to create a superuser - a user account that has control over everything on the site. Go back to the command line, type 
python manage.py createsuperuser, and press enter.

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


# Deploy!

Until now, your website was only available on your computer. Now you will learn how to deploy it! Deploying is the process of publishing your application on the Internet so people can finally go and see your app. :)

#Git


Git is a "version control system" used by a lot of programmers. This software can track changes to files over time so that you can recall specific versions later. A bit like the "track changes" feature in word processor programs (e.g., Microsoft Word or LibreOffice Writer), but much more powerful.


# Starting our Git repository


command-line
$ git init
Initialized empty Git repository in ~/djangogirls/.git/
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com


it's a good idea to use a git status command before git add or whenever you find yourself unsure of what has changed. This will help prevent any surprises from happening, such as wrong files being added or committed. The git status command returns information about any untracked/modified/staged files, the branch status, and much more. The output should be similar to the following:

command-line
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .gitignore
        blog/
        manage.py
        mysite/
        requirements.txt

nothing added to commit but untracked files present (use "git add" to track)


And finally we save our changes. Go to your console and run these commands:

command-line
$ git add --all .
$ git commit -m "My Django Girls app, first commit"
 [...]
 13 files changed, 200 insertions(+)
 create mode 100644 .gitignore
 [...]
 create mode 100644 mysite/wsgi.py


Pushing your code to GitHub
Go to GitHub.com and sign up for a new, free user account. (If you already did that in the workshop prep, that is great!) Be sure to remember your password (add it to your password manager, if you use one).

Then, create a new repository, giving it the name "my-first-blog". Leave the "initialize with a README" checkbox unchecked, leave the .gitignore option blank (we've done that manually) and leave the License as None.




Now we need to hook up the Git repository on your computer to the one up on GitHub.

Type the following into your console (replace <your-github-username> with the username you entered when you created your GitHub account, but without the angle-brackets -- the URL should match the clone URL you just saw):

command-line
$ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
$ git push -u origin master


# Setting up our blog on PythonAnywhere


----> Sign up for a PythonAnywhere account

----> Creating a PythonAnywhere API token


Deploying a web app on PythonAnywhere involves pulling down your code from GitHub, and then configuring PythonAnywhere to recognise it and start serving it as a web application. There are manual ways of doing it, but PythonAnywhere provides a helper tool that will do it all for you. Let's install it first:

PythonAnywhere command-line
$ pip3.6 install --user pythonanywhere


Now we run the helper to automatically configure our app from GitHub. Type the following into the console on PythonAnywhere (don't forget to use your GitHub username in place of <your-github-username>, so that the URL matches the clone URL from GitHub):

PythonAnywhere command-line
$ pa_autoconfigure_django.py https://github.com/<your-github-username>/my-first-blog.git




As you watch that running, you'll be able to see what it's doing:

Downloading your code from GitHub
Creating a virtualenv on PythonAnywhere, just like the one on your own computer
Updating your settings file with some deployment settings
Setting up a database on PythonAnywhere using the manage.py migrate command
Setting up your static files (we'll learn about these later)
And configuring PythonAnywhere to serve your web app via its API


The main thing to notice right now is that your database on PythonAnywhere is actually totally separate from your database on your own computer, so it can have different posts and admin accounts. As a result, just as we did on your own computer, we need to initialize the admin account with createsuperuser. PythonAnywhere has automatically activated your virtualenv for you, so all you need to do is run:

PythonAnywhere command-line
(ola.pythonanywhere.com) $ python manage.py createsuperuser

Now, if you like, you can also take a look at your code on PythonAnywhere using ls:

PythonAnywhere command-line
(ola.pythonanywhere.com) $ ls
blog  db.sqlite3  manage.py  mysite requirements.txt static
(ola.pythonanywhere.com) $ ls blog/
__init__.py  __pycache__  admin.py  apps.py  migrations  models.py
tests.py  views.py


# What is a URL

Every page on the Internet needs its own URL. This way your application knows what it should show to a user who opens that URL. In Django, we use something called URLconf (URL configuration). URLconf is a set of patterns that Django will try to match the requested URL to find the correct view.

Your first Django URL!
Time to create our first URL! We want 'http://127.0.0.1:8000/' to be the home page of our blog and to display a list of posts.

We also want to keep the mysite/urls.py file clean, so we will import URLs from our blog application to the main mysite/urls.py file.

Go ahead, add a line that will import blog.urls. You will also need to change the from django.urls… line because we are using the include function here, so you will need to add that import to the line.

Your mysite/urls.py file should now look like this:

mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]


blog/urls.py
from django.urls import path
from . import views


#Django views – time to create!


blog/views.py
OK, let's open up this file in our code editor and see what's in there:

blog/views.py
from django.shortcuts import render

# Create your views here.
Not too much stuff here yet.

Remember that lines starting with # are comments – this means that those lines won't be run by Python.

Let's create a view as the comment suggests. Add the following minimal view below it:

blog/views.py
def post_list(request):
    return render(request, 'blog/post_list.html', {})
As you can see, we created a function (def) called post_list that takes request and will return the value it gets from calling another function render that will render (put together) our template blog/post_list.html.


