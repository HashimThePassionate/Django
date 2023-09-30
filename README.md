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
1. Clone your github repository
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

### Assume you are using linix and want to use same django project which is already upload on github 
Follow these steps
- Create a github repository finally clone it
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
open your views 
```
polls/views.py¶
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
1. This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
2. To create a URLconf in the App directory, create a file called urls.py. Your app directory should now look like.
<!-- 
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
 -->
### In the App/urls.py file include the following code:
```
from django.urls import path
from . import views
urlpatterns = [
    path("",views.myview, name="myView"),
]
```
### The next step is to point the root URLconf at the project.urls module.
1. In project/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

#### Regards Muhammad Hashim