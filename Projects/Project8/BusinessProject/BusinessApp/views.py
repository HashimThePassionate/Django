from django.shortcuts import render , redirect
from .forms import contact
from .models import Student
from django.contrib import messages
# Create your views here.
def home(request):
    n1 = "Welcome to  Django"
    n2 = "Home Page"
    n3 = """Every cup of our quality artisan coffee starts with locally sourced, 
    hand picked ingredients. Once you try it, our coffee will be a blissful addition 
    to your everyday morning routine - we guarantee it!"""
    n4 = "Visits today!"
    d = {'n1':n1,'n2':n2,'n3':n3,'n4':n4}
    return render(request,'index.html',d)
def about(request):
    n1 = "Welcome to About Section"
    n2 = "Django About"
    n3 = """Founded in 1987 by the Hernandez brothers, our establishment has been serving up rich coffee sourced from artisan farmers in various regions of South and Central America. We are dedicated to travelling the world, 
    finding the best coffee, and bringing back to you here in our cafe.
    We guarantee that you will fall in lust with our decadent blends the moment you walk inside until you finish your last sip. Join us for your daily routine, an outing with friends, or simply just to enjoy some alone time."""
    d = {'n1':n1,'n2':n2,'n3':n3}
    return render(request,'about.html',d)

def product(request):
    n1 = "Welcome to Product Section"
    n2 = "Django Latest Prducts"
    n3 = """We take pride in our work, and it shows. Every time you order a beverage from us, we guarantee that it will be an experience worth having. Whether it's our world famous Venezuelan Cappuccino, a refreshing iced herbal tea, or something as simple as a cup of speciality sourced black coffee, you will be coming back for more."""
    n4 = "DELICIOUS TREATS, GOOD EATS"
    n5 = "BAKERY & KITCHEN"
    n6 = "FROM AROUND THE WORLD"
    n7 = "BULK SPECIALITY BLENDS"
    d = {'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5,'n6':n7}
    return render(request,'products.html',d)

def store(request):
    n1 = "COME ON IN"
    n2 = "WE'RE OPEN"
    n3 = "1116 Orchard Street"
    n4 = "Golden Valley, Minnesota"
    n5 = "Call Anytime"
    n6 = "(317) 585-8468"
    d = {'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5}
    return render(request,'store.html',d)

def success(request):
    return render(request,'success.html')

def simpleForm(request):
    if request.method =='POST':
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['student_name']
            email = form.cleaned_data['student_email']
            course = form.cleaned_data['student_course']
            s = Student(student_name=name,student_email=email,student_course=course)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Thank You, your data has been submitted")
            # return render(request,'success.html',{'name':name})
    else:
        form = contact(auto_id=True)
    objstudent = Student.objects.all()
    return render(request,'Simpleform.html',{'form':form,'student':objstudent})

def delete(request,id):
    db = Student.objects.get(pk=id)
    try:
        db.delete()
    except:
        print("Did not work")
    return redirect('/simple/')

def update(request,id):
    row = Student.objects.get(pk=id)
    if request.method =='POST':
        form = contact(request.POST,instance=row)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your Data has been changed Successfully!")
    else:
        form = contact(instance=row)
         
    return render(request,'update.html',{'form':form})
        
