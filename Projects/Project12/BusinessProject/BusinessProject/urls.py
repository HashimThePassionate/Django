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
from django.urls import path, include
from BusinessApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('simple/',views.simpleForm, name='contactus'),
    path('success/',views.success),
    path('dynamic/<int:id>',views.dynamic, name="dynamic"),
    path('student/',views.student,name="student"),
    path('delete/<int:id>',views.delete ,name="delete"),
    path('edit/<int:id>/',views.update ,name="update"),
    path('signup/',views.reg ,name="signup"),
    path('login/',views.login ,name="login"),
    path('profile/',views.profile ,name="profile"),
    path('logout/',views.logout_profile ,name="logout"),
    path("security/",views.changepassword,name="changepassword"),
    path("edit/",views.UserEdit,name="edit"),
]
