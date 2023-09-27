# Django Project Repository

Welcome to the Django project repository. This repository contains a Django web steps by step guide.

## Getting Started

Follow these instructions to clone the repository and set up your development environment.

### Cloning the Repository

To clone this repository to your local machine, use the following steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:

```
git clone https://github.com/HashimThePassionate/Django.git
```

### Steps to install Django globally:
1. Install Python 3. Django is a Python framework, so you will need Python 3 installed on your machine. You can download Python from the Python website here is the link https://www.python.org/downloads/.
2. Install pip. pip is a package manager for Python that is used to install Django. If you have Python 3 installed, pip should already be installed. You can check by running the following command in a terminal:
```
pip --version
```
If pip is not installed, you can install it using the following command:
```
python3 -m pip install pip
```
### Install Django Globally

If you want to install Django globally on your system, follow these steps:

1. Open your terminal or command prompt.
2. Run the following command:

```
pip install django
```
3. Verify your Django installation. Once Django has been installed, you can verify your installation by running the following command in a terminal:
```
django-admin --version
```
If you see the version of Django that you installed, then Django has been installed successfully

### To uninstall Django globally, follow these steps:

1. Open a terminal window.
2. To uninstall Django, run the following command:
```
pip uninstall django
```
3. Verify that Django has been uninstalled. To verify that Django has been uninstalled, run the following command:
```
pip list
```

### Install Django in Virtual Environment
1. To install virtualenvwrapper-win, which is a virtual environment management tool for Windows, Install virtualenvwrapper-win using pip: 
2. Run the following command to install virtualenvwrapper-win:
```
pip install virtualenvwrapper-win
```
3. After installing virtualenvwrapper-win, you can create a virtual environment for your Django project. Open a Command Prompt and run the following command
```
mkvirtualenv myenv
```
Replace myenv with the name you want to give to your virtual environment.
4. To activate the virtual environment, use the workon command:
```
workon myenv
```
5. With your virtual environment activated, you can use pip to install Django
```
pip install Django
```
6. To deactivate the virtual environment when you're done working on your Django project, simply use the deactivate command

### Uninstall Django in Virtual Environment
1. If your virtual environment is not already active, activate it first. Depending on your operating system:
On Windows:
```
workon Myenv
```
2. Once your virtual environment is active, you can use pip to uninstall Django:
```
pip uninstall Django
```
3. Deactivate the Virtual Environment:
```
deactivate
```

### Complete uninstall virtualenvwrapper-win
1. Run the following command 
```
pip uninstall virtualenvwrapper-win
```
2. if you want to remove only virtualenv run the following command
```
rmvirtualenv myenv
```

###  Create a Django Project
1. Once Django is installed, you can create a Django project using the following command:
```
django-admin startproject projectname
```
### After Creating Project projectname we see these levels
<!-- 
projectname
    |____ projectname
    |        |___ __init__.py   
    |        |___ asgi.py
    |        |___ settings.py
    |        |___ urls.py
    |        |___ wsgi.py
    |____ manage.py 
-->
### __init__.py file
This folder which contains __init__ file is considered as python package.

### wsgi.py file
WSGI (Web Server Gateway Interface) is a specification that describes how a web server communicates with web applications. WSGI provies synchronous Python App.

### asgi.py file
ASGI (Asynchronous Server Gateway Interface) it provides both synchronous and Asynchronous Python App.

### Settings.py file
This files contains all the information or data about project settings
e.g. Database Configuration, Template install, Validation etc.

### urls.py file
This file contains information of url attached with application.

### manage.py file
manage.py atomatically created in each django project. It is a django commandline utility also sets DJANGO_SETTINGS_MODULE environment variable so that it can points to your django project's settings file.

### How to run server
1. Open your command prompt or terminal.
2. Navigate to the root directory of your Django project. This is the directory that contains the manage.py file.
3. To start the development server, run the following command:
```
python manage.py runserver
```
4. to quit server run the following command 
On windows
```
crtl + c
```
### Setup Database in Django 
1. To connect a MySQL database server to your Django project, you need to configure the database settings in your project's.
2. settings.py file. Additionally, you'll want to make sure you have the MySQL Python connector (usually referred to as mysqlclient)
3. Install the MySQLClient run the following command
```
pip install mysqlclient
```
4. Configure the Database Setting 
Open your Django project's settings.py file and locate the DATABASES configuration. Update the settings to connect to your MySQL database. Here's an example configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee',          # Replace with your database name
        'USER': 'root',              # Replace with your database user
        'PASSWORD': 'root',          # Replace with your database password
        'HOST': 'localhost',         # Replace with your database host (e.g., 'localhost' or an IP address)
        'PORT': '3306',              # Replace with your database port (MySQL default is 3306)
    }
}

```
5. Apply Database Migrations
After configuring the database settings, you'll need to apply migrations to create the database tables based on your Django models. Run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

### How to Create and Start Application
A Django project contain one or more applications inside project.
Steps to create applications
1. Go to Project Folder
2. Run the following command
```
python manage.py startapp admission
```
3. creating multiple applications 
run the following commands
```
python manage.py startapp admission
python manage.py startapp student
python manage.py startapp teacher
```

### Installing Application in our Project
1. Open settings.py file and add apps name in INSTALLLED_APPS section 
```
INSTALLED_APPS [
    'django.contrib.admin',
    'course',
    'admission',
    'teacher',
]
```

### Application Directory Structure 
<!-- 
course 
    migrations
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
 -->

### migrations 
This folder contains __init__ file to convert folder to package, and it also contains all flies which are created when running makemigration commands.

### __init__.py
Convert folders files to package

### admin.py file
This file is used to register sql tables so we could perform CRUD operations from admin application. admin application is provided by django to perform CRUD operations.

### apps.py file
This file is used to config app

### models.py file 
This file is used to create our own model later these classes will be converted into database table by django 

### tests.py file
This files is used to create tests

### views.py file
This file contain all about business logic

#### Regards Muhammad Hashim