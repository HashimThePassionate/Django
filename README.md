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

### Now We need to install django in virtual Environment with requirements.txt to control version control
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

### Now lets send back data  too Client 
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
### In the App/urls.py file include the following code:
```
from django.urls import path
from SimpleApp import views
urlpatterns = [
    path("",views.index, name="home"),
]
```
### The next step is to point the root URLconf at the project.urls module.
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

1. defines a view
```
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
def home(request):
    name = "muhammad Hashim"
    age = 20
    list1 = [1,2,3]
    list2 = [4,5,6]
    django = "I'm using django"
    dj = "Django"
    D = datetime.now()
    value = 123456789
    f = 34.23234
    list3 = [  {"name": "Zahid", "age": 19},{"name": "Ahmed", "age": 22},{"name": "Jamshed", "age": 31},]
    d = {'name':name, 'age':age, 'list1':list1, 'list2':list2, 'django':django, 'dj':dj, 'D':D,'list3':list3,'value':value, 'f':f}
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
</body>
</html>
```
- #### Note: if you want to  learn more about it please visit https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference
#### Regards Muhammad Hashim