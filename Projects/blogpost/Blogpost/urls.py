"""
URL configuration for Blogpost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name="home"),
    path('about/', views.about_page,name="about"),
    path('blog/', views.blog_page,name="blog"),
    path('contact/', views.contact_page,name="contact"),
    path('signup/', views.signup_page,name="signup"),
    path('signin/', views.signin_page,name="signin"),
    path('signout/', views.signout_page,name="signout"),
    path('AddPost/', views.addBlog_page,name="addpost"),
    path('delete/<int:id>',views.delete_page, name='delete'),
    path('update/<int:id>',views.update_page, name='update'),
]
