from django.shortcuts import render
<<<<<<< HEAD
from .forms import studentForm
from .models import student
from django.http import HttpResponseRedirect 
# from .forms import contactform
=======
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
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

def contact(request):
    return render(request,'contact.html')
<<<<<<< HEAD
def success(request):
    return render(request,'success.html')

def simpleForm(request):
    myForm = studentRegistration(auto_id=True,label_suffix=':',initial= {'name':'Muhammad','email':'hashim@gmail.com'})
    myForm.order_fields(field_order=['email','name'])
    d = {'form':myForm}
    return render(request,'Simpleform.html',d)
    from django.contrib.auth.hashers import make_password

def fo(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['student_name']
            e = form.cleaned_data['student_email']
            c = form.cleaned_data['student_course']
            studentObj = student(student_name=n,student_email=e,student_course=c)
            studentObj.save()
            # return render(request,'success.html',{'name':n})
            return HttpResponseRedirect('/success/')
    else:
        form = studentForm()
    return render(request,'Simpleform.html',{'form':form})

def stu(request):
    return render(request,'student.html')

def studentdetail(request,id):
    if id == 1:
        name = "Zain"
        age = 23
        course = "Python"
        progress = "hard worker"
        s = {'n':name,'age':age,'c':course,'p':progress}

    if id == 2:
        name = "Wahab"
        age = 19
        course = "Python"
        progress = "hard worker"
        s = {'n':name,'age':age,'c':course,'p':progress}

    if id == 3:
        name = "Yonis"
        age = 19
        course = "Python"
        progress = "hard worker"
        s = {'n':name,'age':age,'c':course,'p':progress}

    return render(request,'studentdetail.html',s)
=======

def success(request):
    return render(request,'success.html')

from django.contrib.auth.hashers import make_password
from .models import user
from .forms import contactform
def simpleForm(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            pw = form.cleaned_data['password']
            hp = make_password(pw)
            reg = user(name=nm,password=hp)
            reg.save()
            # form = contactform(auto_id=True)
            return render(request,'success.html',{'name':nm}) 
    else:
        print("Empty Form with with GET Method")
        form = contactform(auto_id=True)
        # print(form)
    return render(request,'Simpleform.html',{'form':form})
>>>>>>> f70a6a7f5382a5a39c22d5f759bbee8cada889d1
