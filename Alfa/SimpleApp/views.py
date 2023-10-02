from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("<h3>Hello This is our first App just for Practice </h3>")

def home(request):
    name = "Muhammad Hashim"
    age = 23
    d = {'name':name, 'age':age}
    return render(request, 'index.html', d)
