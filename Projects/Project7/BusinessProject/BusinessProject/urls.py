"""
URL configuration for BusinessProject project.

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
from BusinessApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('contact/',views.contact, name='contactus'),
<<<<<<< HEAD
    path('simple/',views.simpleForm, name='simpleform'),
    path('form/',views.fo, name='formus'),
    path('success/',views.success, name='success'),
    path('student/',views.stu, name='student'),
    path('studentdetail/<int:id>/',views.studentdetail, name='studentdetail'),
=======
    path('simple/',views.simpleForm, name='simpleus'),
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
]
