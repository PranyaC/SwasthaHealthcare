from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from health.forms import ContactForm, BlogForm, SignupForm
from . import models
# Create your views here.

def home(request):
    return render(request, "index.html")

#user authentication and registration
def login_users(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            return redirect("login")
    else:
        return render(request, "login.html")

def logout_users(request):
    logout(request)
    return redirect("home")

def signup_users(request):
    if request.method=="POST":
        data=SignupForm(request.POST)
        if data.is_valid():
            new_user=data.save()

            login(request, new_user)
            return redirect('home')
    else:
        data=SignupForm()

    return render(request, "registration.html", {"form":data})

def blog(request):
    try:
        data=models.Blog.objects.all()
        context={"data":data}
    except Exception as e:
        context={"data":"No Data"}  
    return render(request, "blog-post-list.html", context)

def blogadd(request):
    form=BlogForm()
    if request.method == 'POST':
        myData=BlogForm(request.POST)
        if myData.is_valid():
            myData.save()
            return redirect('home')
    context={"data":form}
    return render(request,'blog-create.html',context)

def blogdelete(request, id):
    data=models.Blog.objects.get(id=id)
    data.delete()
    return redirect('blog')

def blogupdate(request, id):
    data=models.Blog.objects.get(id=id)
    updateform=BlogForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        
        return redirect('blog')
    context={"data":updateform}
    return render(request,'blog-create.html',context)


def contact(request):
    try:
        data=models.Contact.objects.all()
        context={"data":data}
    except Exception as e:
        context={"data":"No Data"}
    return render(request, "contact-us.html", context)

def contactadd(request):
    form=ContactForm()
    if request.method == 'POST':
        myData=ContactForm(request.POST)
        if myData.is_valid():
            myData.save()
            return redirect('contact')
    context={"data":form}
    return render(request,'contact-us.html',context)

def aboutus(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'service-page.html')

def gallery(request):
    return render(request, 'gallery.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def blogpost(request):
    return render(request, 'blog-post.html')

def findus(request):
    return render(request, 'slider.html')

def faq(request):
    return render(request, 'faq.html')