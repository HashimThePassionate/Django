from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def product(request):
    return render(request, "products.html")
def store(request):
    return render(request, "store.html")