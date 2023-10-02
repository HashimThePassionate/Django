from django.urls import path
from SimpleApp import views
urlpatterns = [
    # path("",views.index, name="home"),
    path("",views.home, name="home"),
]
