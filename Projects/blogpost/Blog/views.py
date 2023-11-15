from django.shortcuts import render, redirect
from Blog.forms import contact, sigupContactForm, signin   ,BlogForm
from Blog.models import contactTable, Blog
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, logout, update_session_auth_hash, login
# Create your views here.
def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def blog_page(request):
    if request.user.is_authenticated:
        get = Blog.objects.all()
        return render(request,'post.html',{'blog':get})
    else:
        return redirect('/signin/')
    
def addBlog_page(request):
    if request.user.is_authenticated:
            if request.method =='POST':
                form = BlogForm(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    des = form.cleaned_data['des']
                    CT = Blog(title=title,des=des)
                    CT.save()
                    return redirect('/blog/')
            else:
                form = BlogForm(auto_id=True)
            return render(request,'addBlog.html',{'form':form})
    else:
        return redirect('/signin/')
     
def delete_page(request,id):
    db = Blog.objects.get(pk=id)
    try:
        db.delete()
    except:
        return ('/blog/')
    return redirect('/blog/')

def update_page(request,id):
    row = Blog.objects.get(pk=id)
    if request.method =='POST':
        form = BlogForm(request.POST,instance=row)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = BlogForm(instance=row)
    return render(request,'addBlog.html',{'form':form})


def contact_page(request):
    return render(request,'contact.html')

def contact_page(request):
    if request.method =='POST':
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneno = form.cleaned_data['phoneno']
            message = form.cleaned_data['message']
            CT = contactTable(name=name,email=email,phoneno=phoneno,message=message)
            CT.save()
            messages.add_message(request,messages.SUCCESS,"Thank You For Contacting Us, we will get back soon!")
    else:
        form = contact(auto_id=True)
    return render(request,'contact.html',{'form':form})


def signup_page(request):
    if request.method == "POST":
        form =  sigupContactForm(request.POST)
        if form.is_valid():
            user=form.save()
            get = Group.objects.get(name='Editor')
            user.groups.add(get)
            messages.add_message(request,messages.SUCCESS,"Congratulations Your Account Has Been CreatedSuccessfully!")
    else:
        # form =csigupContactForm()
        form =  sigupContactForm()
    return render(request,'signup.html',{'form':form})

def signin_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signin(request=request.user,data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user) 
                        return redirect('/blog/')
            else:
              return redirect('/signin/')
                    
        else:
            form = signin()
    else:
         return redirect('/blog/')
    return render(request,'signin.html',{'form':form})

def signout_page(request):
    logout(request)
    return redirect('/signin/')
