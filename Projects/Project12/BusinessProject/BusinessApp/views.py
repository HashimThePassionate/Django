from django.shortcuts import render ,redirect
from .forms import contact, customregistration
from .models import Student
# from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth import login as auth_login 
from django.http import HttpResponse
# from django.conf import settings

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
    Studentobj = Student.objects.all()
    if request.method =='POST':
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['student_name']
            email = form.cleaned_data['student_email']
            course = form.cleaned_data['student_course']
            s = Student(student_name=name,student_email=email,student_course=course)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Your Data has been submitted Successfully!")
            # return render(request,'success.html',{'name':name})
            # return HttpResponseRedirect('/success/')
    else:
        form = contact(auto_id=True)
    return render(request,'Simpleform.html',{'form':form,'student':Studentobj})


def dynamic(request,id):
    if id == 1:
        name = "Muhammad Hashim"
        techstack = "Django"
        student = {'id':id,'n':name,"t":techstack}
    if id == 2:
        name = "Wahab"
        techstack = "Full Stack Django"
        student = {'id':id,'n':name,"t":techstack}
    if id == 3:
        name = "Zain"
        techstack = "Hacker"
        student = {'id':id,'n':name,"t":techstack}
    return render(request,'dynamic.html',student)

def student(request):
    return render(request,'student.html')

def delete(request,id):
    if request.method == 'POST':
        obj = Student.objects.get(pk=id)
        obj.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    obj = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = contact(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/success/')
    else:
        form = contact(instance=obj)
    return render(request,'update.html',{'form':form})


def send_email(user_email):
    subject = "Registration Confirmation"
    message = "Hey! 👋,\n\nThank you for registering on our website!"
    from_email = 'warriorecosystem346@gmail.com'
    recipient_list = [user_email,]
    # send_mail(subject,message,from_email,recipient_list,fail_silently=False)
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def reg(request):
    if request.method == "POST":
        form =  customregistration(request.POST)
        # form=customregistration(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user=form.save()
            messages.add_message(request,messages.SUCCESS,"Congratulations Account Created Successfully!")
            # send_email(user.email)
            return redirect('signup')
    else:
        # form =customregistration()
        form =  customregistration()
    return render(request,'signup.html',{'form':form})

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        auth_login(request, user) 
                        return HttpResponseRedirect('/profile/')
            else:
              return HttpResponse("Sorry Invalid")
                    
        else:
            form = AuthenticationForm()
    else:
         return HttpResponseRedirect('/profile/')
    return render(request,'login.html',{'form':form})

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def logout_profile(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form =  PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.add_message(request,messages.SUCCESS,"Password Change Successfully!")
                return redirect('/profile/')
        else:
            form =  PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':form,'name':request.user})
    else:
        return redirect('/login/')

        