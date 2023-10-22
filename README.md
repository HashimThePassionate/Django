# Welcome to my GitHub Django Zero to Hero repository!
## Table of Contents
- [Cloning the Repository](#Cloning-the-Repository)
- [Steps to install Django globally](#Steps-to-install-Django-globally)
- [Install Django Globally](#Install-Django-Globally)
- [To uninstall Django globally](#To-uninstall-Django-globally)
- [Install Django in Virtual Environment](#Install-Django-in-Virtual-Environment)
- [Uninstall Django in Virtual Environment](#Uninstall-Django-in-Virtual-Environment)
- [Complete uninstall virtualenvwrapper-win](#Complete-uninstall-virtualenvwrapper-win)
- [Create a Django Project](#Create-a-Django-Project)
- [How to run servert](#How-to-run-server)
- [Setup MYSQL Database in Django](#Setup-MYSQL-Database-in-Django)
- [Setup PostgreSQL Database in Django ](#Setup-PostgreSQL-Database-in-Django)
- [How to Create and Start Application](#How-to-Create-and-Start-Application)
- [Installing Application in our Project](#Installing-Application-in-our-Project)
- [install django in virtual Environment with requirements file to control version control](#install-django-in-virtual-Environment-with-requirements-file-to-control-version-control)
- [Command to check django installation folder](#Command-to-check-django-installation-folder)
- [Write your first view](#Write-your-first-view)
- [Urls Pattern in Project level urls.py](#Urls-Pattern-in-Project-level-urls.py)
- [Urls Patterns inside  in Application  urls.py](#Urls-Patterns-inside-in-Application-urls.py)
- [Create dynamic templates folder inside root directory](#Create-dynamic-templates-folder-inside-root-directory)
- [Create dynamic templates folder inside Application](#Create-dynamic-templates-folder-inside-Application)
- [Lets explore Django built in filters](#Lets-explore-Django-built-in-filters)
- [Built-in template tags](#Built-in-template-tags)
- [Create static folder inside root project](#Create-static-folder-inside-root-project)
- [Django Template Inheritance / Template Extending](#Django-Template-Inheritance-/-Template-Extending)
- [url tag](#url-tag)
- [Include tag](#Include-tag)
- [What is Model in Django](#What-is-Model-in-Django)
- [Create your own Model Class](#Create-your-own-Model-Class)
- [Steps to uae model to create table](#Steps-to-uae-model-to-create-table)
- [Create a model Timing open models](#Create-a-model-Timing-open-models-file-inside-application-directory)
- [Admin Application](#Admin-Application)
- [Creating a super user](#Creating-a-super-user)
- [How to register model](#How-to-register-model)
- [str method](#str-method)
- [ModelAdmin display all data in the interface](#ModelAdmin-display-all-data-in-the-interface)
- [Register Model by Decorator](#Register-Model-by-Decorator)
- [Django Form](#Django-Form)
- [Creating a django form using form class](#Creating-a-django-form-using-form-class)
- [Display form to user](#Display-form-to-user)
- [Add form tag and submit button manually in template Simpleform html file](#Add-form-tag-and-submit-button-manually-in-template-Simpleform-html-file)
- [Please note some important points](#Please-note-some-important-points)
- [Configure id attribute](#Configure-id-attribute)
- [Configure label tag](#Configure-label-tag)
- [Dynamic initial values](#Dynamic-initial-values)
- [Ordering a form](#Ordering-a-form)
- [Render Form field manually](#Render-Form-field-manually)
- [Loop Form](#Loop-Form)
- [Form Fields](#Form-Fields)
- [Field Arguments](#Field-Arguments)
- [Fields Arguments Example forms in application level](#Fields-Arguments-Example-forms-in-application-level)
- [Widget](#Widget)
- [Built-in Widgets](#Built-in-Widgets)
- [GET and POST ](#GET-and-POST )
- [What is Cross Site Request Forgery](#What-is-Cross-Site-Request-Forgery)
- [Here how CSRF protection using tokens work](#Here-how-CSRF-protection-using-tokens-work)
- [Get Django Form Data](#Get-Django-Form-Data)
- [Get Django form Data in CMD Terminal](#Get-Django-form-Data-in-CMD-Terminal)
- [Built-in Fields ](#Built-in-Fields)
- [Custom Cleaning and Validating Specific Field](#Custom-Cleaning-and-Validating-Specific-Field)
- [Validation of Complete Django Form at once ](#Validation-of-Complete-Django-Form-at-once)
- [Save Form Data in Database](#Save-Form-Data-in-Database)


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

### Steps to install Django globally
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

### To uninstall Django globally

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
<pre>
projectname
    |____ projectname
    |        |___ __init__.py   
    |        |___ asgi.py
    |        |___ settings.py
    |        |___ urls.py
    |        |___ wsgi.py
    |____ manage.py 
</pre>

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
### Setup MYSQL Database in Django
Make Sure to download MySQL Server, MySQL Workbench
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
### Setup PostgreSQL Database in Django 
1. Download postgresql from https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
2. Install Postgresql and pgadmin create password
3. After installing open pgAdmin4 under servers find PostgreSQL 16, write click to connect server write down password and click ok to connect postgreSQL Server.
4. right click to database and click on query tool, SQL command interface will be open simple create your database using this query
```
CREATE DATABASE employee;
```
4. its times to install psycopg2 library to connect python with postgreSQL environment.
5. if you are using virtual environment simply activate it and install this library.
```
pip install psycopg2
```
6. Now its time to setup database, simply open your settings.py file in project level and paste this code in DATABASE portion.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Employee',    # Replace with your database name
        'USER': 'postgres',    # Replace with your database user
        'PASSWORD': 'root',    # Replace with your database password
        'HOST': 'localhost',   # Replace with your database host ('localhost')
        'PORT': '2000',        # Replace with your database port 
    }
}
```
- Congratulations your postgreSQL database has been sucessfully connected

### How to Create and Start Application
A Django project contain one or more applications inside project.
Steps to create applications
1. Go to Project Folder
2. Run the following command
```
django-admin startapp admission
```
3. creating multiple applications 
run the following commands
```
django-admin  startapp admission
django-admin  startapp student
django-admin  startapp teacher
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
<pre>
course 
    migrations
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
</pre>

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

### install django in virtual Environment with requirements file to control version control
- Follow these steps
```
pip install virtualenvwrapper-win
mkvirtualenv V
workon V
pip install Django
django-admin startproject MyProject
cd MyProject
python manage.py startapp Apple
pip freeze > requirements.txt
```
### We Assume that you created a Web Application now its time to upload to github
1. Create a github repository
2. Clone your github repository
```
git clone https://github.com/HashimThePassionate/example.git
cd example
```
2. Copy project file to example directory
3. finally push everything
```
git add .
git commit -m "initial"
git push origin main
```
Congratulations your code has been pushed

### Assume you are using linux and want to use same django project which is already upload on github 
Follow these steps
```
git clone https://github.com/HashimThePassionate/example.git
cd example
cd djangoProject
pip install virtualenvwrapper-win
mkvirtualenv myenv
workon myenv
pip install -r requirements.txt
```
All the requirements packages will install atomatically

### Before we deep dive in views and url route we first need to discuss http and how http works
What is HTTP? 
HTTP (Hypertext Transfer Protocol) is a fundamental protocol of the World Wide Web (WWW) that defines how data is transmitted and exchanged between a client (usually a web browser) and a web server. HTTP is the protocol that powers the web, and it's responsible for the retrieval and display of web pages, as well as the exchange of various web resources like text, images, videos, and more. Here are the steps involved in how HTTP works:
1. Client Request: The process begins when a user opens a web browser and enters a URL (Uniform Resource Locator) into the address bar. The URL specifies the web page or resource they want to access. For example, the URL might be something like.
2. DNS Resolution: If the URL contains a domain name (e.g., www.example.com), the browser needs to resolve this domain name to an IP address using the Domain Name System (DNS). DNS is a distributed system that maps human-readable domain names to IP addresses. Once the IP address is obtained, the browser can contact the web server.
3. Establishing a TCP Connection: HTTP typically runs over TCP (Transmission Control Protocol). The browser initiates a TCP connection to the web server on the specified port (usually port 80 for HTTP and port 443 for HTTPS). This is the beginning of a communication channel between the client (browser) and the server.
4. HTTP Request: The client (browser) sends an HTTP request to the web server. The request consists of:
- A request method (e.g., GET, POST, PUT, DELETE) that indicates the desired action.
- The requested resource's path (e.g., /index.html).
- Headers containing additional information about the request (e.g., user-agent, accepted content types).
- Optionally, a message body (used in POST and PUT requests to send data to the server).
5. Server Processing: The web server receives the HTTP request, processes it, and determines how to respond. It locates the requested resource (e.g., the HTML file) on its filesystem or generates dynamic content through server-side scripting (e.g., PHP, Python, Ruby).
6. HTTP Response: The server constructs an HTTP response containing:
- A status code (e.g., 200 for success, 404 for not found, 500 for server error).
- Response headers (e.g., content-type, date, server).
- The response body, which contains the actual content (e.g., HTML, images, JSON data).
7. Sending the Response: The server sends the HTTP response back to the client through the established TCP connection.
8. Client Rendering: The client (browser) receives the response and processes it. If the response is an HTML file, the browser renders it, which includes parsing HTML, applying CSS styles, and executing JavaScript code.
9. Additional Requests: If the HTML file references additional resources (e.g., CSS, JavaScript, images), the browser issues additional HTTP requests to fetch those resources. This can lead to a series of requests and responses to fully render a web page.
10. Closing the Connection: Once all resources are fetched, or if the client or server decides to close the connection, the TCP connection is closed, freeing up network resources.

### Now lets look a practical example 
look the http url 
```
https://data.pr4e.org/page1.htm
```
Now we want to explore request headers, response headers, and body

### python provides built in socket lets write a script and explore all the above things run this script building a simple web browser.
```
import socket

# Server information
server_host = 'data.pr4e.org'
server_port = 443 # HTTPS typically uses port 443

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to {server_host}:{server_port}")

    # Send an HTTP GET request
    request = "GET /page1.htm HTTP/1.0\r\n\r\n"
    client_socket.sendall(request.encode())

    # Receive and print data from the server in a loop
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode(), end='')

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the socket
    client_socket.close()
    print("\nSocket closed")

```
After running the script you should see everything in response of header 

### Lets Building a simple HTTP Web Server 
```
from socket import *
def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += """<html><body><p> <b>Hello</b> <i>and</i> <strong>Welcome</strong> This is <u>our</u> X <sup>2</sup> Simple Html course
        <marquee  direction="right" style="color: green;">In The Next Course we cover Styling using CSS</marquee>
        and after that we move to dynamic manipulation using JavaScript</p><br>
    <a href="https://www.google.co.uk/" target="_blank"><img src="https://images.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="" width="200px"></a><br>
    <a href="https://www.linkedin.com/in/hashimthepassionate/" target="_blank">Hashim</a><br>
    <a href="mailto:hashiimtahir@gmail.com" target="_blank">hashiimtahir@gmail.com</a><br>
    <a href="tel:+923075239903" target="_blank">Call Me</a>
    <ol type="i" start="5">
        <li>Apple</li>
        <li>Grapes</li>
        <li>Strawberry</li>
    </ol>
    <ul type="square">
        <li>Apple</li>
        <li>Grapes</li>
        <li>Strawberry</li>
    </ul>
    <dl>
        <dt>HTML Stand For</dt>
        <dd>
            HyperText Markup Language
        </dd>
    </dl></body></html>\r\n\r\n"""
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)
    serversocket.close()
print('Access http://localhost:9000')
createServer()
```
Run this code and see how the web server response in a client request

### Now lets send back data too Client 
```
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
print("response")
mysock.close()
```
### Command to check django installation folder
```
pip show django
```
### Write your first view
open your app  views.py file and paste the view as a function
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h3>Hello This is our first App just for Practice </h3>")
```

### Urls Pattern in Project level urls.py
1. Simple open your project  level urls.py file and find urlpatterns list variable and mention your view in path variable, make sure to import views from your app
```
from django.contrib import admin
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index),
]
```

### now run your server with simple this code
```
python manage.py runserver
```
1. Now here is the point, when you run the server you will see error like 
<pre>
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/
Using the URLconf defined in Alfa.urls, Django tried these URL patterns, in this order:
admin/
home/
The empty path didn’t match any of these.
You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
</pre>
2. This error tells that you url is not found to fix this paste this url 
```
http://127.0.0.1:8000/home/
```
3. Now when you look the url pattern you, will see i mention /home/ after the url bcz when i define the url i clearly mention 'home/' in  urlpatterns variable so to access this we must mention this url
http://127.0.0.1:8000/home/
4. Now we need to define a default url pattern than what we do, here is the example go to urls.py and paste this code
```
from django.contrib import admin
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
]
```
5. Now when you run the server you will see the url is working default.

### Urls Patterns inside  in Application  urls.py
1. Simply create view in views.py in app level
```
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h3>Hello This is our first App just for Practice </h3>")
```
2. now create urls.py in app level directory. To create a URLconf in the App directory, create a file called urls.py. Your app directory should now look like.
<pre>
App/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
</pre>
3. open urls.py and paste this code
4. This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
### In the App/urls.py file include the following code
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.index, name="home"),
]
```
### The next step is to point the root URLconf at the project.urls module
1. In project/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Template 
1. A Template is a text file, it can generate any text-based format (HTML, CSV, XML etc)
2. A template contains variables, which get replaced with values when the template is evaluated, and tages, which control the logic of template.
3. Template is used by view function to represent the data to user.
4. User sends request to view then view contact template after that view get information from the template and then view gives response to user.

### Create dynamic templates folder inside root directory
1. Simply create "templates" directory inside project folder 
<pre>
projectname/
├── projectname/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   |__ templates
|      |___ home.html
|      |___ about.html
|      |___ contact.html
|      |___ blog.html
├── manage.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
</pre>

### Simply create home.html file inside templates directory 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Div </title>
</head>
<body>
    <article>
        <h2>Google Chrome</h2>
        <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
    </article>
    <details>
        <summary>Epcot Center</summary>
        <p>Hi,{{name}} How are you? Your age is {{age}}</p>
    </details>
    <p>I have a date on <time datetime="2008-02-14 20:00">Valentines day</time>.</p>
</body>
</html>
```
### Add "TEMPLATE_DIR" in settings.py 
```
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],//Add TEMPLATE_DIR here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### What is render() function 
1. When you call render(), it combines the provided template with a context dictionary (containing data to be inserted into the template) and generates an HTML response.
- render()- It combines a given template with a given context dictionary and returns an Httpresponse object with that rendered text.
<pre>
Syntax:
    render(request,template_name, context = dict_name, using = None)
Where,
request -- The object used to generate this response.
template_name -- The full name of a template to use or sequence of templates names, if a sequence is given, the first template thats exists will be used.
context -- A dictionary of values to add to the template context. By default, this is an empty dictionary. if a value in the dictionary is callable, the view will call just before rendering the template.
using -- The NAME of a template engine to use for  loading the template.
</pre>
### Define views to render html
```
def home(request):
    name = "Muhammad Hashim"
    age = 23
    d = {'name':name, 'age':age}
    return render(request, 'index.html', d)
```
### define urlpattern in app level urls.py
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home, name="home"),
]
```
### finally add url to root project urls.py
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Now its time to render html
```
python manage.py runserver
```
- Here is how to access home page
<pre>
http://127.0.0.1:8000/home/
</pre>

### Create dynamic templates folder inside Application
1. Create templates directory inside application and inside templates create another directory with same application name and inside it create html files, the result should be link this.
<pre>
projectname/
├── projectname/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── myapp/
    |__ templates
    |  |___ home.html
    |  |___ about.html
    |  |___ contact.html
    |  |___ blog.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   |__ __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
</pre>

### Define views
```
from django.shortcuts import render
def home(request):
    name = "Muhammad Hashim"
    age = 23
    d = {'name':name, 'age':age}
    return render(request, 'SimpleApp/index.html', d)
```

### Define urls in Application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
### Define urls in Project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('SimpleApp.urls')),
]
```
### Create html document inside application  templates / folder / index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Div </title>
</head>
<body>
    <article>
        <h2>Google Chrome</h2>
        <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
    </article>
    <details>
        <summary>Epcot Center</summary>
        <p>Hi,{{name}} How are you? Your age is {{age}}</p>
    </details>
    <p>This is just a simple paragraph</p>
</body>
</html>
```

### Lets explore Django built in filters
1. When we need to modify variable before displaying we can use filters. Pipe symbol | is used to apply filter.
<pre>
Syntax:
      {{variable | filter}}
Some filters takes arguments
Syntax:
      {{variable | filter : argument}}
</pre>

### filters Example
#### Filters list
- add
- addslashes
- capfirst
- date
- dictsort
- filesizeformat
- first
- floatformat
- length
- linenumbers
- escape

1. defines a view
```
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
multiString ="""One
two
three
four"""
def home(request):
    name = "muhammad Hashim"
    age = 20
    list1 = [1,2,3]
    list2 = [4,5,6]
    django = "I'm using django"
    dj = "Django"
    nick = "MUHAMMAD"
    D = datetime.now()
    value = 123456789
    f = 34.23234
    messages = 1
    welcome = "&quotWelcome&quot to &#x27;&ltDjango&gt;&#x27; Programming"
    list3 = [  {"name": "Zahid", "age": 19},{"name": "Ahmed", "age": 22},{"name": "Jamshed", "age": 31},]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f, "m":multiString, 'nick':nick, 'messages': messages , 'w':welcome}
    return render(request, 'SimpleApp/index.html', d)
```
2. urls.py in application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
3. urls.py in project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SimpleApp.urls')),
]
```
4. rendering document
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Built-in Filters</title>
</head>
<body>
<section>
<h2>Google Chrome</h2>
<p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
</section>
<p>Hi,{{name|capfirst}} How are you? Your age is {{age|add:"3"}}</p>
<pre>
First list :{{list1}}

Second list : {{list2}}

The Sum of two list is {{list1|add:list2}}
</pre>
<p>{{django|addslashes}}</p>
<p>"{{dj|center:"15"}}"</p>
<p>{{D|date:"j s l n M Y"}}</p>
<pre>
Without sorted List:
{{list3}} 

With sorted list:
{{list3|dictsort:"name"}}
</pre>
<p>This is just a simple paragraph</p>
<p>if value is {{value}} than the output will be {{value|filesizeformat}} </p>
<p>The {{list1}} list first item is {{list1|first}}</p>
<p>The value {{f}}</p>
<p>The value {{f|floatformat}}</p>
<p>The value {{f|floatformat:"3"}}</p>
<p>My name {{name|capfirst}} contains {{name|length}} letters</p>
<pre>
{{m}}

{{m|linenumbers}}
</pre>
<pre>
Name in Captial letter : {{nick}}

Name in lower letter : {{nick|lower}}
</pre>
<p>Rendered text date: "{{D|date:"l" }}"</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
</pre>
<span style="font-size:30px;">Django Templates tags</span>
<pre>{% autoescape off %}
{{w}}
{{w|escape}}
{% endautoescape %}</pre>
</body>
</html>
```
- #### Note: if you want to  learn more about it please visit https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference

### Built-in template tags
1.  comment
2.  if tag
- if tags with boolean operators
- - and, or, not
- - == operator
- - in operator
- - if tag with filter
3. lorem
<pre>
Displays random “lorem ipsum” Latin text. This is useful for providing sample data in templates.

Usage:
{% lorem [count] [method] [random] %}
The {% lorem %} tag can be used with zero, one, two or three arguments. The arguments are:
Argument	Description
count	A number (or variable) containing the number of paragraphs or words to generate (default is 1).
method	Either w for words, p for HTML paragraphs or b for plain-text paragraph blocks (default is b).
random	The word random, which if given, does not use the common paragraph (“Lorem ipsum dolor sit amet…”) when generating text.
Examples:
{% lorem %} will output the common “lorem ipsum” paragraph.
{% lorem 3 p %} will output the common “lorem ipsum” paragraph and two random paragraphs each wrapped in HTML <p> tags.
{% lorem 2 w random %} will output two random Latin words.
</pre>
4. now
```
It is {% now "jS F Y H:i" %}
```
- The {% if %} tag evaluates a variable, and if that variable is “true” (i.e. exists, is not empty, and is not a false boolean value) the contents of the block are output:
5. For tag
- Syntax
<pre>
{% for itemvariable in variable %}
{{itemvariable}}
{% endfor %}
Example:
<ul>
{% for itemvariable in variable %}
<li>{{itemvariable}}</li>
{% endfor %}
</ul>
</pre>
5. regroup
- regroup¶
Regroups a list of alike objects by a common attribute.
- This complex tag is best illustrated by way of an example: say that cities is a list of cities represented by dictionaries containing "name", "population", and "country" keys
<pre>
cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"},
]
and you’d like to display a hierarchical list that is ordered by country, like this:
. India
  . Mumbai: 19,000,000
  . Calcutta: 15,000,000
. USA
  . New York: 20,000,000
  . Chicago: 7,000,000
. Japan
  . Tokyo: 33,000,000
You can use the {% regroup %} tag to group the list of cities by country. The following snippet of template code would accomplish this:
</pre>
6. cycle
- Produces one of its arguments each time this tag is encountered. The first argument is produced on the first encounter, the second argument on the second encounter, and so forth. Once all arguments are exhausted, the tag cycles to the first argument and produces it again.


1. Views
```
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
multiString ="""One
two
three
four"""
def home(request):
    name = "muhammad Hashim"
    age = 20
    list1 = [1,2,3]
    list2 = [4,5,6]
    django = "I'm using django"
    dj = "Django"
    nick = "MUHAMMAD"
    D = datetime.now()
    value = 123456789
    f = 34.23234
    messages = 1
    welcome = "&quotWelcome&quot to &#x27;&ltDjango&gt;&#x27; Programming"
    list3 = [  {"name": "Zahid", "age": 19},{"name": "Ahmed", "age": 22},{"name": "Jamshed", "age": 31},]
    list4 = ["Hashim","Juniad","Usman","Zahid"]
    cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"}]
    coach_list = [
        {
            'name': 'junaid',
            'athletes': [
                {'name': 'Hassan'},
                {'name': 'Hamza'},
                {'name': 'Zubair'},
            ]
        },
        {
            'name': 'Jamshed',
            'athletes': [
                {'name': 'Ehtisham'},
                {'name': 'Ahsan'},
                {'name': 'Zeeshan'},
            ]
        },
    ]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f, "m":multiString, 'nick':nick, 'messages': messages , 'w':welcome, 'nl':list4, 'cities':cities,'c':coach_list}
    return render(request, 'SimpleApp/index.html', d))
```
2. urls.py in application level
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.home),
]
```
3. urls.py in project level
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SimpleApp.urls')),
]
```
4. rendering document
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <meta http-equiv="refresh" content="05"> -->
    <title>Built-in Filters</title>
</head>
<body>
<p>Rendered text date: "{{D|date:"l" }}"</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
</pre>
{% comment %} if Tag {% endcomment %}
<pre>{% if name %}
Number is: {{ name|capfirst }}
{% endif %}
</pre>
<pre>{% if n %}Number is: {{ name|capfirst }}
{% else %}no name available{% endif %}
</pre>
{% comment %} If tag with and operator {% endcomment %}
<pre>
{% if name and age  %}
Your Name is {{name}} and Age is {{age}}
{% else %}
No name and age available
{% endif %}
</pre>
{% comment %} if tag with == operator {% endcomment %}
<pre>
{% if age == 23 %}
Your age is  {{age}}
{% else %}
try again
{% endif %}
</pre>
{% comment %} if tag with == "string" {% endcomment %}
<pre>
{% if name == "muhammad Hashim" %}
Your name is : {{name}}
{% endif %}
</pre>
{% comment %} if tag with in operator {% endcomment %}
<pre>
{% if "Dj" in "Django" %}
true it is present
{% endif %}
</pre>
{% comment %} if tag with filter {% endcomment %}
<pre>
{% if name|length >= 14 %}
You have lots of messages today!
 {% endif %}
</pre>
{% comment %}  if tag with random text {% endcomment %}
<p>
{% lorem 50 w random %}
</p>
<p>
    It is {% now "jS F Y H:i" %}
</p>
{% comment %} for loop {% endcomment %}
{% for n in name %}
<li>{{n}}</li>
{% endfor %}
{% comment %} regroup tag {% endcomment %}
{% regroup cities by country as country_list %}
<ul>
{% for country in country_list %}
    <li>{{ country.grouper }}
    <ul>
        {% for city in country.list %}
          <li>{{ city.name }}: {{ city.population }}</li>
        {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>
{% comment %} cycle tag {% endcomment %}
{% for o in list1 %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
{% comment %} resetcycle tag {% endcomment %}
{% for coach in c %}
    <h1>{{ coach.name }}</h1>
    {% for athlete in coach.athletes%}
        <p class="{% cycle 'odd' 'even' %}">{{ athlete.name }}</p>
    {% endfor %}
    {% resetcycle %}
{% endfor %}
</body>
</html>
```
### Static Files
1. CSS files, JavaScript files, images files, video files are considered static files in django.
1. Django provides django.contrib.staticfiles to help you manage them.
3. django.contrib.staticfiles collect static files from each of your applications 

### Create static folder inside root project
1. Create static directory inside root project 
2. Inside static folder, create required folders which will contains all static files respectively like css folder, js folder and images folder etc

### Here is how we created
<pre>
Alfa/
├── Alfa/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   
|   |__ static
|      |___ images
|          |___ favicon.io
|          |___ horse.jpg
|      |___ CSS
|          |___ style.css
|      |___ JS
|          |___ script.js
|
|   |__ templates
|      |___ index.html
├── manage.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py   
</pre>

### Add static in settings.py
1. add the following code snipped in settings.py
2. import os if not imported
```
import os
STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR,'static')
# print(STATIC_URL)
# print(STATIC_DIR)
STATICFILES_DIRS = [STATIC_DIR]
# print(STATICFILES_DIRS)
```

### Use static files in templates
1. first load static files for serve
2. Reference static files


### This is our index.html file code
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Home Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <a href="#" class="logo">My Website</a>
                <ul class="nav-links">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
        </nav>
        <div class="hero">
            <div class="container">
                <h1>Welcome to My Website</h1>
                <p>Your trusted source for amazing content.</p>
                <a href="#" class="cta-button">Learn More</a>
            </div>
        </div>
    </header>
    <main class="main-content">
        <section class="about">
            <div class="container">
                <h2>About Us</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam id justo at magna dapibus tristique.</p>
            </div>
        </section>
        <section class="services">
            <div class="container">
                <h2>Our Services</h2>
                <div class="service">
                    <h3>Service 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
                <div class="service">
                    <h3>Service 2</h3>
                    <p>Nullam id justo at magna dapibus tristique.</p>
                </div>
                <div class="service">
                    <h3>Service 3</h3>
                    <p>Phasellus gravida dolor in consectetur tincidunt.</p>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 My Website. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```
#### Note We suppose that views and urls are already define, so we can directly jump to our main topic

### style.css 
```
/* Reset some default styles for consistency */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Apply some global styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Style the header */
.header {
    background-color: #333;
    color: #fff;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
}

.logo {
    font-size: 24px;
    text-decoration: none;
    color: #fff;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin-right: 20px;
}

.nav-links a {
    text-decoration: none;
    color: #fff;
}

/* Style the hero section */
.hero {
    background-image: url('hero-background.jpg');
    background-size: cover;
    text-align: center;
    padding: 100px 0;
    color: #fff;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 40px;
}

.cta-button {
    display: inline-block;
    padding: 15px 30px;
    background-color: #ff6600;
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.cta-button:hover {
    background-color: #ff9900;
}

/* Style the main content sections */
.main-content {
    background-color: #fff;
    padding: 40px 0;
}

.about, .services {
    margin-bottom: 40px;
}

.about h2, .services h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

.service {
    margin-bottom: 20px;
}

.service h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Style the footer */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}
```
### Now its time to load static
1. here is updated index.html 
```
<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Home Page</title>
    <link rel="stylesheet" href='{% static "css/style.css" %}'> 
    <link rel="shortcut icon" href='{% static "images/favicon.ico" %}' type="image/x-icon">
</head>
<body>
    <header class="header">
        <nav class="navbar">
            <div class="container">
                <a href="#" class="logo">My Website</a>
                <ul class="nav-links">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
        </nav>
        <div class="hero">
            <div class="container">
                <h1>Welcome to My Website</h1>
                <p>Your trusted source for amazing content.</p>
                <a href="#" class="cta-button">Learn More</a>
            </div>
        </div>
    </header>
    <main class="main-content">
        <section class="about">
            <div class="container">
                <h2>About Us</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam id justo at magna dapibus tristique.</p>
            </div>
        </section>
        <section class="services">
            <div class="container">
                <h2>Our Services</h2>
                <div class="service">
                    <h3>Service 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
                <div class="service">
                    <h3>Service 2</h3>
                    <p>Nullam id justo at magna dapibus tristique.</p>
                </div>
                <div class="service">
                    <h3>Service 3</h3>
                    <p>Phasellus gravida dolor in consectetur tincidunt.</p>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 My Website. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```
### here is updated style.css
1. just update images to relative path
```
.hero {
    background-image: url('../images/horse.jpg');
    background-size: cover;
    text-align: center;
    padding: 100px 0;
    color: #fff;
}
```
### Django Template Inheritance / Template Extending
1. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.
2. The "extends" is used to inherit template.
3. Extends tag tells the template engine that this template "extends" another template.
4. {% extends %} 

<pre>
Syntax
{% extends 'parent_template' %}
{% extends variable %}
Example:
{% extends "./base.html" %}
{% extends "../base.html" %}
</pre>
5. {% block %} - The block tag is used for overriding specific part of a template.

<pre>
Syntax
{% block blockname %} ....... {% endblock %}
{% block blockname %} ....... {% endblock endblockname %}
Example:
{% block title %} ....... {% endblock %}
{% block content %} ....... {% endblock content %}
</pre>

6. Rules
- If we use {% extends %} in a template, it must be the first template tag in that template. Template inheritance won't work otherwise.
- More {% block %} tags in our base template is better.
- if we need to get the content of the block from the parent template, the {{ block.super }} variable will do the trick.

#### Note Now to better understand lets check in the projects directory, and inside projects directory find project3 for extends tag and block tag.

### url tag
1. {% url %} - it returns an absolute path reference matching a given view and optional parameters.
- path (route, view, kwargs = none, name = None)
<pre>
Syntax
{% url 'urlname' %}
{% url 'urlname' as variable %}
Example: views.py
def home(request):
    return render(request, "home.html")
Example: urls.py
urlpatterns = [
    path('home/' , views.home, name ="Home")
]
Example index.html
<a href ="{% url 'Home' %}">Home</s>
</pre>

#### Note see project3 for url tag

### Include tag
1. {% include tag %} Tag - It loads template and renders it with current context, This is a way of "including" other templates within template. Each include is a completely independent rendering process.
<pre>
Syntax
{% include "header.html" %}
{% include 'footer.html' %}
</pre>
2. See in projects directory, under projects directry see project4, we use include and extend both tags within that project.

### What is Model in Django
1. A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.
2. Model class is a class which represent a table in database, each model is a python class that subclasses django.db.models.Model.
3. Each attribute of the model represents a database field
4. With all of this, Django gives you an automatically-generated database-access API. Django provides built-in database by default that is sqlite database.
5. We can use other database like mysql, postgresql etc. 

### Lets first setup database, in my example i used mysql see this section 
- [Setup MYSQL Database in Django](#Setup-MYSQL-Database-in-Django)

### Create your own Model Class
1. models.py file which is inside application folder, is required to create our own model class
2. Our own model class will inherit Python's model class.
<pre>
Syntax
class ClassName(models.Model):
    field_Name = models.FieldType(args, options)

Example: (models.py) 
from django.db import models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
</pre>

### Steps to use model to create table
1. Once you have defined your models, you need to tell django you are going to use those model.
- Open settings.py file
- Write app name which contains model.py file in INSTALLED_APPS = []
- Open Terminal
- Run python manage.py makemigrations
- Run python manage.py migrate

2. Migrations
- Migrations are Djnago way's of propagating changes you make to your models 
- makemigrations: This is responsible for creating new migrations based on the changes you have made to your models.
- migrate: This is responsible for applying and unapplying migrations.
- sqlmigrate: This displays the SQL statements for migration
- showmigrations: This lists a project's migrations and their status

3. Display SQL Statements 
- We can retrieve SQL statement by using below command:
<pre>
Syntax
python manage.py sqlmigrate applicationName dbfileName
Example:
python manage.py sqlmigrate CasualApp 0001
</pre>
#### Note: File name can be found inside application's migrations folder.

### Create a model Timing open models file inside application directory
```
from django.db import models
class Timing(models.Model):
    day = models.CharField(max_length=50, unique=True)
    opening_hours = models.CharField(max_length=100)
```

### Now run this command to create a table 
```
python manage.py makemigrations CasualApp
```
- After running this command you will see this 
<pre>
Migrations for 'CasualApp':
  CasualApp\migrations\0001_initial.py
    - Create model Time
</pre> 
- Now lets migrate sql to create a table
```
python manage.py sqlmigrate CasualApp 0001
```
your output look like this
<pre>
Create model Time
------------------------------------------------------
CREATE TABLE `CasualApp_time` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `day` varchar(50) NOT NULL UNIQUE, `opening_hours` varchar(100) NOT NULL);
------------------------------------------------------
</pre>
```
python manage.py migrate 
```
- Finally Migrate all changes
<pre>
Operations to perform:
  Apply all migrations: CasualApp, admin, auth, contenttypes, sessions
Running migrations:
  Applying CasualApp.0001_initial... OK
</pre>

### Now insert some data using sql raw insert query, open mysql cmd or mysql worbench 
1. In my case open mysql workbench, connect to  database server, finally use database which you connected in your settings.py and use that database. open sql query in mysql workbench.
2. Write this sql query
```
INSERT INTO CasualApp_time (day, opening_hours) VALUES
    ('Sunday', 'Closed'),
    ('Monday', '7:00 AM to 8:00 PM'),
    ('Tuesday', '7:00 AM to 8:00 PM'),
    ('Wednesday', '7:00 AM to 8:00 PM'),
    ('Thursday', '7:00 AM to 8:00 PM'),
    ('Friday', '7:00 AM to 8:00 PM'),
    ('Saturday', '9:00 AM to 5:00 PM');

```
### Now define a view to collect database data and pass as a dictionary views.py in application
```
from CasualApp.models import Time
def store(request):
    n1 = "COME ON IN Restaurant"
    n2 = "WE'RE OPEN"
    n3 = "1116 Orchard Street"
    n4 = "Golden Valley, Minnesota"
    n5 = "Call Anytime"
    n6 = "(317) 585-8468"
    time = Time.objects.all()
    d = {'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'T':time}
    return render(request,'store.html',d)
```

### Now to display that data in index file 
```
{% if T %}
<ul class="list-unstyled list-hours mb-5 text-left mx-auto">
{% for t in T  %}
<li class="list-unstyled-item list-hours-item d-flex">
    {{t.day}}
    <span class="ms-auto">{{t.opening_hours}}</span>
</li>
{% endfor %}
{% else %}
<li class="list-unstyled-item list-hours-item d-flex">
    No Timing Available
</li>
</ul>
```
### Admin Application
1. It is built-in application provided by Django.
2. This application provides admin interface for CRUD operations without writing sql statements.
3. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site.
4. Admin application can be accessed using ```http://127.0.0.1:8000/admin```
5. Super user is required to login into admin application.

### Creating a super user
- createsuperuser command is used to create super user.
```
python manage.py createsuperuser
```
- After running this command you see message like this
<pre>
Username (leave blank to use 'dell'): Hashim
Email address: hashiimtahir@gmail.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
</pre>

### How to register model
1. We are registering our table which we has created using model class, to default admin interface.
2. Steps to register follows:
- Open admin.py file which is inside application directory.
- Import your own Model class created inside Application's models.py file.
- admin.site.register(ModelClassName)

<pre>
Example:
Open admin.py
From CasualApp.models import Time
admin.site.register(Time)
</pre>

### str method
1. The __str__() method is called whenever you call str() on an object. To display an object in Django admin site and as the value inserted into a template when it displays an object. Thus, you shiuld always return a nice, human-readable representation of the model from the __str__() method.
2. Write this method in your own model class which is inside models.py file.
<pre>
Syntax
def __str__(self):
    return self.fieldName
Example:
def __str__(self):
    return self.day
</pre>
#### Note  __str__() method only display one field to display all the field use ModelAdmin

### ModelAdmin display all data in the interface
1. The ModelAdmin class is the representation of a model in the admin interface.
2. To show table's all the data in the admin interface we have to create ModelAdmin class in the admin.py of application directory.
3. list_display() 
- list_display to control which fields are displayed on the change list page of admin. if you don't set list_display, the admin site will display a single column that display the __str__() representation of each object.  
<pre>
Syntax: Creating ModelAdmin class in admin.py
class ModelAdminClassName(admin.ModelAdmin):
    list_display=('fieldname1','fieldname2', ....... so on)
Register above created class
admin.site.register(ModelClassName,ModelAdminClassName)

Example: admin.py
from django.contrib import admin
from CasualApp.models import Time
class TimeAdmin(admin.ModelAdmin):
    list_display=('day','opening_hours')
admin.site.register(Time,TimeAdmin)
</pre>

### Register Model by Decorator
1. A decorator can be used to register modelAdmin classes.
<pre>
Syntax:
@admin.register(ModelClassName1,ModelClassName2, .....)
Example: admin.py
from django.contrib import admin
from CasualApp.models import Time
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display=('day','opening_hours')
</pre>

### Django Form
1. Model Form
2. Form API

- Django form: Django's form functionality can simplify and automate vast portions of work like data prepared for display in a form, rendered as HTML, edit using a convenient interface, returned to the server, validated and cleaned up etc and do it more securely than most programmers would be able to do in code they wrote themselves.
Django handles three different parts of work.
1. Preparing and restructering data to make it ready for rendering.
2. Creating HTML forms for the data.
3. receiviing and processing submitted forms and data from the client.

### Creating a django form using form class
1. To create a django form we have to create a new file inside application directory, lets say file name is forms.py, now we can write some code inside forms.py file.
<pre>
from django import forms
Syntax:
class formClassName(forms.Form):
    label=froms.FieldType()
    label=forms.FieldType(label='label_name')
</pre>
2. Here is example
```
from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
```

### Display form to user
1. Create an object of form class in views.py then pass object to templates file.
2. Use form object in template file.

### Creating form object in views.py file
```
from django.shortcuts import render
from .forms import studentRegistration
def showdata(request):
    myForm = studentRegistration()
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
```

### Pass it to Simpleform.html file
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple</title>
</head>
<body>
    <h1>Simple Form</h1>
    {{form}}
</body>
</html>
```
#### Note: Form object won't provide form tag and button you have to write them manually in a template.

### Add form tag and submit button manually in template Simpleform html file
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple</title>
</head>
<body>
    <h1>Simple Form</h1>
    <form action="">
    {{form}}
    <input type="submit" value="submit">
    </form>
   
</body>
</html>
```
#### Please note some important points
- The output does not include the <table>...</table> tags, nor does not it innclude the <form>...</form> tags or an  <input type="submit"> tags, its your job to do it.
- Each field type has a default HTMl representation, CharField is represented by an <input type="text">
and EmailField by <input type="email">.
- The HTML name for each tag is directly from its attribute name in the studentRegistration class.
- The text label for each field e.g, 'Name' and 'Email' is generated  from the field name by converting all the underscores to spaces and upper-casing the first letter.
- Each text label is surrounded in an HTML <label> tag, which points to the appropriate form field via its ids. 
- Its id, in turn is generated by prepending 'id_' to the field name. The id attributes and <label> tag included in the output by default.

### Configure id attribute
- auto_id: The id attribute values are generated by prepending id_ to the forms field names, This behavior is configurable though.
- Use the auto_id argument to the form constructor to control the id and label behavior. This argument must be true,false or string. By default, auto_id is set to the string 'id_%s'
1. if auto_id is set to string containing the format character '%s' then the form output will include <label> tags, and will generate id attributes based on the format string.
2. if auto_id is set to be true, then the form output will include <label> tags and will use the field name as its id for each form field.
3. if auto_id is false, then the form output will not include <label> tags nor id attributes.

```
from django.shortcuts import render
from .forms import studentRegistration
def showdata(request):
    myForm = studentRegistration(auto_id='my_%s')
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
```

### Configure label tag
1. Label_suffix - A translatable string (defaults to a colon (:) in English) that will be appended after any label name when a form is rendered.
```
from django.shortcuts import render
from .forms import studentRegistration
def simpleForm(request):
    myForm = studentRegistration(auto_id=True,label_suffix=':')
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
```

### Dynamic initial values
1. initial is used to declare value of forms fields at runtime.
2. To accomplish this, use the initial argument to a form, This argument, if given, should be a dictionary mapping field names to initial values.

```
from django.shortcuts import render
from .forms import studentRegistration
def simpleForm(request):
    myForm = studentRegistration(auto_id=True,label_suffix=':',initial= {'name':'Muhammad','email':'hashim@gmail.com'})
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
```

### Ordering a form
1. order_fields(field_order) - This method is used to rearrange the fields any time with a list of field names as in field_order by default it is none.
```
from django.shortcuts import render
from .forms import studentRegistration
def simpleForm(request):
    myForm = studentRegistration(auto_id=True,label_suffix=':',initial= {'name':'Muhammad','email':'hashim@gmail.com'})
    myForm.order_fields(field_order=['email','name'])
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
```
### Render Form field manually
1. Each field is available as an attribute of the form using {{form.name_of_field}}
- {{field.label}} example : {{form.name.label}}
2. Field label tags
- Example {{form.name.label_tag}}
3. id tag
- {{form.id_for_label}}
4. Field value
- Example {{form.name.value}}
5. field as html 
- Example {{form.name.html_name}}
6. field help text
- Example {{form.name.hrlp_text}}

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple</title>
</head>
<body>
    <h1>Simple Form</h1>
    <form action="">
     <div>
        <label for="{{form.name.id_for_label}}">Name</label>
        {{form.name}}
        {{form.email.label_tag}}
        {{form.email}}
        <input type="submit" value="submit">
    </div>
    </form>
</body>
</html>
```
### Loop Form
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple</title>
</head>
<body>
    <h1>Simple Form</h1>
    <form action="">
        {% for f in form %}
        {{f.label_tag}}
        {{f}}
        {% endfor %}
        <input type="submit" value="submit">
    </form>
   
</body>
</html>
```
### Form Fields
A form's fields are themselves classes, they manage form data and perform validation when a form is submitted.
<pre>
Syntax:
FieldType(**kwargs)

Example:
IntegerField()
EmailField()
CharField()
</pre>

### Simple Example
```
from django import forms
class studentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    number=forms.IntegerField()
```

### Field Arguments
1. Field.required
-  By default, each Field class assumes the value is required, so if you pass an empty value – either None or the empty string ("") – then clean() will raise a ValidationError exception.
2. Label
- The label argument lets you specify the “human-friendly” label for this field. This is used when the Field is displayed in a Form.
3. label_suffix
- The label_suffix argument lets you override the form’s label_suffix on a per-field basis.
4.  initial
- The initial argument lets you specify the initial value to use when rendering this Field in an unbound Form.
5. widget
- The widget argument lets you specify a Widget class to use when rendering this Field. See Widgets for more information.
6. help_text
- The help_text argument lets you specify descriptive text for this Field. If you provide help_text, it will be displayed next to the Field when the Field is rendered by one of the convenience Form methods (e.g., as_ul()).
7. error_messages
- The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override. For example, here is the default error message.
8. validators
- The validators argument lets you provide a list of validation functions for this field.
9. disabled
- The disabled boolean argument, when set to True, disables a form field using the disabled HTML attribute so that it won’t be editable by users. Even if a user tampers with the field’s value submitted to the server, it will be ignored in favor of the value from the form’s initial data.

### Fields Arguments Example forms in application level
```
from django import forms
import datetime as d
class studentRegistration(forms.Form):
    first_name=forms.CharField(initial="Muhammad",error_messages={"required": "Please enter your first name"})
    last_name=forms.CharField(required=False,initial="Hashim")
    full_name=forms.CharField(label="Good Name",help_text="Maximum 100 Character of length",max_length=100)
    email=forms.EmailField(initial="hashiimtahir@gmail.com")
    num=forms.IntegerField(required=False,initial=93075239903)
    url=forms.URLField(required=False,label="Your Website",initial="https://www.google.com")
    date=forms.DateField(initial=d.date.today,help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
```
### Fields Arguments Example views.py in application level
```
def simpleForm(request):
    default_data = {'first_name':'Ali','last_name':'Ahmed','full_name':'Ali Ahmed','email':'aliahmed@gmail.com','url':'https://www.yahoo.com'}
    default_empty = {'first_name':'','last_name':'','full_name':'','email':'','url':''}
    # if you pass initial value as a dictionary than form.py initial value will be ignore
    form = studentRegistration(default_empty,auto_id=True)
    d = {'form':form} 
    print(form)
    return render(request,'Simpleform.html',d)
```

### Fields Arguments Example template Simpleform.html in project level
```
<div style="background-color:white; padding:30px 50px">
    <h1>Simple Form</h1>
    <div>
      <form action="" novalidate>
        {% for f in form %}
        {{f.label_tag}}
        {{f}} <br><br>
        {% endfor %}
          <input type="submit" value="submit"><br><br>
      </form>
    </div>
    <form action="">
      {{form.as_p}} 
      <input type="submit" value="submit">
    </form>
</div>
```

### Fields Arguments Example urls.py in project level level
```
from django.urls import path
from BusinessApp import views
path('simple/',views.simpleForm, name='simpleus'),
```

### Widget
1. A widget is Django's representation of an HTML input element.
2. The widget handles the rendering of the HTML, and the extraction of data a GET/POST dictionary that corresponds to the widget.
3. Example are TextInput, Textarea
4. A dictionary containing HTML attributes to be set on the rendered widget.
If you assign a value of True or False to an attribute, it will be rendered as an HTML5 boolean attribute.
- Example : 
<pre>
feedback=forms.CharField(widget=forms,TextInput(attrs={'class':'somecss1 somecss2',
'id':'uniqueid'}))
</pre>

### Built-in Widgets
1. TextInput - It renders as: 
- Example: TextInput - It renders as: <input type="text"...>
<pre>
name = forms.CharField(widget=forms.TextInput)
</pre>
2. NumberInput - It renders as: 
- Example: NumberInput - It renders as: <input type="number"...>
<pre>
name = forms.CharField(widget=forms.NumberInput)
</pre>
3. EmailInput - It renders as: 
- Example: EmailInput - It renders as: <input type="email"...>
<pre>
name = forms.CharField(widget=forms.EmailInput)
</pre>
4. URLInput - It renders as: 
- Example: URLInput - It renders as: <input type="url"...>
<pre>
name = forms.CharField(widget=forms.URLInput)
</pre>
5. PasswordInput - It renders as: 
- Example: PasswordInput - It renders as: <input type="password"...>
<pre>
name = forms.CharField(widget=forms.PasswordInput)
</pre>
6. HiddenInput - It renders as: 
- Example: HiddenInput - It renders as: <input type="hidden"...>
<pre>
name = forms.CharField(widget=forms.HiddenInput)
</pre>
7. DateInput - It renders as: 
- Example: DateInput - It renders as: <input type="text"...>
<pre>
name = forms.CharField(widget=forms.DateInput)
</pre>

### GET and POST  
- GET should be used only for requests that do not affect the state of the system.
- Any request that could be used to change the state of the system should use POST. 
- GET would also not suitable for a password form, because the password would appear in the URL, and thus, also in browser history and server logs, all in plain text. Neither would it be suitable for large quantities of data, or for binary data, such as an image. A Web application that uses GET requests for admin forms is a security risk: it can be easy for an attacker to mimic a form's request to gain access to sensitive parts of the system.
- POST, coupled with other protections like Django's CSRF protection offers more control over access.
- GET, by contrast, bundles the submitted data into a string, and uses this to compose a URL. The URL contains the address where the data must be sent, as well as the data keys and values
- Django's login form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response.
- GET is suitable for things like a web search form, because the URLs that represek a GET request can easily be bookmarked, shared, or resubmitted. 

### What is Cross Site Request Forgery
CSRF, or Cross-Site Request Forgery, is a type of security vulnerability that occurs when an attacker tricks a user into unknowingly making an unwanted and potentially malicious request to a web application on which the user is authenticated. CSRF attacks can target any action that can be initiated via an HTTP request, such as changing a password, making a purchase, or modifying account settings.
1. The attacker creates a malicious webpage that includes a form or script.
2. The victim, who is logged into a web application, visits the malicious webpage.
3. Without the victim's knowledge, the malicious page sends a request to the web application on which the victim is authenticated.
4. The web application, believing the request is legitimate because it comes from the victim's browser with valid authentication cookies, processes the request.
5. The victim's account is modified or an action is taken without their consent.

#### Here how CSRF protection using tokens work
1. When a user logs in or creates a session, the server generates a random CSRF token and associates it with that user's session.
2. The CSRF token is included in any form presented to the user, typically as a hidden field.
3. When the user submits a form, the server checks if the included CSRF token matches the one associated with the user's session. If it doesn't match, the server rejects the request.
4. The CSRF token is unique to each user and session, making it extremely difficult for attackers to forge valid tokens.

### CSRF Token in Django
- In Django, a popular web framework for Python, CSRF protection is automatically enabled for all HTML forms via middleware. It generates unique CSRF tokens for each user session and verifies the tokens when processing form submissions.

### Get Django Form Data
- Validate Data / Field Validation
- Get Cleaned Data

### Django Form and Field Validation 
1. is valid() - This method is used to run validation and return a Boolean designating whether the data was valid as True or not as False. This returns True or False. 
<pre>
Syntax: views.py
form.is_valid()
</pre>
2. cleaned data — This attribute is used to access clean data. Each field in a Form class is responsible not only for validating data, but also for "cleaning" it normalizing it to a consistent format. This is a nice feature, because it allows data for a particular field to be input in a variety of ways, always resulting in consistent output. Once you've created a Form instance with a set of data and validated it, you can access the clean data via its cleaned_data attribute. 
3. Any text based field such as CharField or EmailField always cleans the input into a string.
4. If your data does not validate, the cleaned_data dictionary contains only the valid fields.
5. cleaned data will always only contain a key for fields defined in the Form, even if you pass extra data when you define the Form. When the Form is valid, cleaned data will include a key and value for all its fields, even if the data didn't include a value for some optional field.

### Get Django form Data in CMD Terminal
### Follow steps
1. Step:1 forms.py
```
from django import forms
class contactform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'exampleid'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'exampleid'}))
```
2. Step:2 Get submitted data in views.py
```
from .forms import contactform
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            print("Form Validated with POST Data")
            print(f'Your Name is ${form.cleaned_data["username"]}')
            print(f'Your password is ${form.cleaned_data["password"]}')
            print("All the input in same way")
            print(form.cleaned_data)
            # form = contactform(auto_id=True)
            # return render(request,'success.html',{'name':name}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
        print(form)
    return render(request,'Simpleform.html',{'form':form})
```
3. Step:3 Render Html form 
```
   <div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                {{ field.label_tag }}
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
```

### Step:4 Success template success.html
```
{% block main%}
{% load static %}
<div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6 mt-5">
        <div class="alert bg-light text-center" role="alert">
          <img src='{% static "assets/img/success.svg" %}' alt="Success Icon" width="64" height="64">
          <h4 class="alert-heading">Hey {{name}}!</h4>
          <p>Your request has been processed successfully.</p>
          <hr>
          <p class="mb-0">Thank you for submit a request.</p>
        </div>
          <a href="{% url 'home' %}" class="btn btn-primary">Back to Home</a>
      </div>
    </div>
  </div>
{% endblock main %}
```
### Built-in Fields 
1. CharField(**kwargs) 
-  Default widget: TextInput 
-  Empty value: Whatever you've given as empty_value. 
-  Normalizes to: A string. Uses MaxLengthValidator and MinLengthValidator if max_length and  min_length are provided. Otherwise, all inputs are valid.
-  Error message keys: required, maxiength, miniength I
-  It has three optional arguments for validation:
-  max length and min length - If provided, these arguments ensure that the string is at most or at least the given length.
-  strip - If True (default), the value will be stripped of leading and trailing whitespace.
-  empty_value - The value to use to represent "empty". Defaults to an empty string.

<pre>Example forms.py</pre>
```
from django import forms
class contactform(forms.Form):
    name=forms.CharField(min_length=5, max_length=10, error_messages={'required':'Please Enter Your Name','min_length':'Your name must be at least 5 characters long','max_length':'Your name cannot exceed 10 characters.'},widget=forms.TextInput(attrs={'class':'form-control','id':'exampleid'})) 
``` 

<pre>Example views.py</pre>
```
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            print("Form Validated with POST Data")
            print(f'Your Name is ${name}')
            print("All the input in same way")
            print(form.cleaned_data)
            return render(request,'success.html',{'name':name}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
    return render(request,'Simpleform.html',{'form':form})
```

<pre>Example Simpleform.html</pre>
```
{% block main%}
<div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                {{ field.label_tag }}
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
{% endblock main %}
``` 

2. BooleanField(**kwargs) 
-  Default widget: CheckboxInput
-  Empty value: False
-  Normalizes to: A Python True or False value.
-  Validates that the value is True (e.g. the check box is checked) if the field has required=True. 
- Error message keys: required.

<pre>Example forms.py</pre>
```
from django import forms
class contactform(forms.Form):
    name=forms.CharField(min_length=5, max_length=10, error_messages={'required':'Please Enter Your Name','min_length':'Your name must be at least 5 characters long','max_length':'Your name cannot exceed 10 characters.'},widget=forms.TextInput(attrs={'class':'form-control','id':'exampleid'}))
    agree=forms.BooleanField(label_suffix='',error_messages={'required':'Please agree to our terms and conditions'},widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label="I agree")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].label = 'I agree'
        self.fields['agree'].label_tag = 'class="form-label"' 
``` 

<pre>Example views.py</pre>
```
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            agree = form.cleaned_data["agree"]
            print("Form Validated with POST Data")
            print(f'Your Name is ${name}')
            print(f'Your are agree Y/n ${agree}')
            print("All the input in same way")
            print(form.cleaned_data)
            return render(request,'success.html',{'name':name}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
    return render(request,'Simpleform.html',{'form':form})
```

<pre>Example Simpleform.html</pre>
```
 <div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                <label for="{{ field.id_for_label }}" class="form-label">
                  {{ field.label}}
                </label>
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary " style="width: 50%; margin:0 250px;">Submit</button>
        </form>
      </div>
    </div>
```

### Custom Cleaning and Validating Specific Field
- clean_<fieldname>0 - This method is called on a form subclass where <fieldname> is replaced with the name of the form field attribute. This method does any cleaning that is specific to that particular attribute, unrelated to the type of field that it is. This method is not passed any parameters. You will need to look up the value of the field in self.cleaned_data and remember that it will be a Python object at this point, not the original string submitted in the form. 

### Cleaning and validating specific field
<pre>forms.py</pre>
```
from django import forms
class contactform(forms.Form):
    name=forms.CharField(min_length=5, max_length=10, error_messages={'required':'Please Enter Your Name','min_length':'Your name must be at least 5 characters long','max_length':'Your name cannot exceed 10 characters.'},widget=forms.TextInput(attrs={'class':'form-control','id':'exampleid'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))
    def clean_password(self):
        p = self.cleaned_data['password']
        if p == 'password' or 'password' in p.lower():
            raise forms.ValidationError('Password should not contain the word "password" ')
    agree=forms.BooleanField(label_suffix='',error_messages={'required':'Please agree to our terms and conditions'},widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label="I agree")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].label = 'I agree'
        self.fields['agree'].label_tag = 'class="form-label"' 
```

<pre>views.py</pre>
```
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            agree = form.cleaned_data["agree"]
            print("Form Validated with POST Data")
            print(f'Your Name is ${name}')
            print(f'Your are agree Y/n ${agree}')
            print("All the input in same way")
            print(form.cleaned_data)
            # form = contactform(auto_id=True)
            return render(request,'success.html',{'name':name}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
        # print(form)
    return render(request,'Simpleform.html',{'form':form})
```
<pre>Simplform.html</pre>
```
 <div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                <label for="{{ field.id_for_label }}" class="form-label">
                  {{ field.label}}
                </label>
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary " style="width: 50%; margin:0 250px;">Submit</button>
        </form>
      </div>
    </div>
```

### Validation of Complete Django Form at once 
1. clean() — The clean() method on a Field subclass is responsible for running to_python(), validate(), and run validators() in the correct order and propagating their errors. . If, at any time, any of the methods raise ValidationError, the validation stops and that error is raised.
2. This method returns the clean data, which is then inserted into the cleaned_data dictionary of the form. Implement a clean() method on your Form when you must add custom validation for fields that are interdependent. 
<pre>
Syntax:- 
Form.clean() 
</pre>

### Validation of Complete Django Form at once Example with password match
<pre>forms.py</pre>
```
from django import forms
class contactform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={"required": "Please enter your name"})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"} )
    matchpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"},label="Password (again)" )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        matchpassword =  cleaned_data.get('matchpassword')
        if password != matchpassword:
            self.add_error('password', 'Password does not match')
            self.add_error('matchpassword', 'Password does not match')
        if name and len(name) < 4:
            self.add_error('name', 'Name should not be less than 4')
        if password and 'password' in password.lower():
            self.add_error('password', 'Password should not contain the word "password"')
    agree=forms.BooleanField(label_suffix='',error_messages={'required':'Please agree to our terms and conditions'},widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),label="I agree")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].label = 'I agree'
        self.fields['agree'].label_tag = 'class="form-label
```

<pre>views.py</pre>
```
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            matchpassword =  form.cleaned_data['matchpassword']
            agree = form.cleaned_data['agree']
            print("Form Validated with POST Data")
            print(f'Your Name is ${name}')
            print(f'Your are agree Y/n ${agree}')
            print(f'Your passwordY/n ${password}')
            print(f'Repeat passwordY/n ${matchpassword}')
            print("All the input in same way")
            print(form.cleaned_data)
            # form = contactform(auto_id=True)
            return render(request,'success.html',{'name':name}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
        # print(form)
    return render(request,'Simpleform.html',{'form':form})
```
<pre>Simpleform.html</pre>
```
    <div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                <label for="{{ field.id_for_label }}" class="form-label">
                  {{ field.label}}
                </label>
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary " style="width: 50%; margin:0 250px;">Submit</button>
        </form>
      </div>
    </div>
```

### Save Form Data in Database
<pre>Open forms.py to define form</pre>
```
from django import forms
class contactform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={"required": "Please enter your name"})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"} )
    matchpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),error_messages={"required": "Please enter password"},label="Password (again)" )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        matchpassword =  cleaned_data.get('matchpassword')
        if password != matchpassword:
            self.add_error('password', 'Password does not match')
            self.add_error('matchpassword', 'Password does not match')
        if name and len(name) < 4:
            self.add_error('name', 'Name should not be less than 4')
        if password and 'password' in password.lower():
            self.add_error('password', 'Password should not contain the word "password"')
```
<pre>Create model user</pre>
```
from django.db import models
class user(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
```
<pre>Make migrations command</pre>
```
python manage.py makemigrations
python manage.py makemigrations BusinessApp
python manage.py migrate
```
<pre>Register model to admin site</pre>
```
from django.contrib import admin
from .models import user
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display=('id','name','password')
```
<pre>View.py to render form </pre>
```
from django.contrib.auth.hashers import make_password
from .models import user
from .forms import contactform
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            pw = form.cleaned_data['password']
            hp = make_password(pw)
            reg = user(name=nm,password=hp)
            reg.save()
            # form = contactform(auto_id=True)
            return render(request,'success.html',{'name':nm}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
        # print(form)
    return render(request,'Simpleform.html',{'form':form})
```
<pre>Simpleform.html file</pre>
```
{% extends "base.html" %}
{% block title %}About{% endblock title %}
{% block main%}
    <div class="container">
      <div style="background-color:white; padding:30px 50px">
        <form action="" method="post" novalidate>
          {% csrf_token %}
          <div class="form-group">
            {% for field in form %}
              <div class="form-group">
                <label for="{{ field.id_for_label }}" class="form-label">
                  {{ field.label}}
                </label>
                {{ field }}
                {% if field.errors %}
                    {{ field.errors|striptags }}
                {% endif %}
              </div>
            {% endfor %}
          </div>
          <button type="submit" class="btn btn-primary " style="width: 50%; margin:0 250px;">Submit</button>
        </form>
      </div>
    </div>
{% endblock main %}
```
<pre>success.html file</pre>
```
{% extends "base.html" %}
{% block title %}Store{% endblock title %}
{% block main%}
{% load static %}
<div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6 mt-5">
        <div class="alert bg-light text-center" role="alert">
          <img src='{% static "assets/img/success.svg" %}' alt="Success Icon" width="64" height="64">
          <h4 class="alert-heading">Hey {{name}}!</h4>
          <p>Your request has been processed successfully.</p>
          <hr>
          <p class="mb-0">Thank you for submit a request.</p>
        </div>
          <a href="{% url 'home' %}" class="btn btn-primary">Back to Home</a>
      </div>
    </div>
  </div>
{% endblock main %}
```

#### Regards Muhammad Hashim