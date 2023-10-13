from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def portfolio(request):
    return render(request,'portfolio-details.html')