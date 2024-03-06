from django.shortcuts import render

# Create your views here.


def our_home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
