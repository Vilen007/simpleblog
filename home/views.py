from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import Contact
from blog.models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    Post = post.objects.all().order_by("-views")[:3]
    return render(request, "home/home.html", {'posts':Post})
def about(request):
    return render(request, "home/about.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST['nam']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']
        if len(name) < 4 and len(lname) < 4 and len(email) < 12 and len(phone) < 7 and len(query) < 4:
            messages.error(request,"Please Enter Valid Information")
        else:
            contact_object = Contact(name=name, lname=lname, email=email, phone=phone, query=query)
            contact_object.save()
            messages.success(request, "Thanks for contacting us! We will get you soon.")
    return render(request, "home/contact.html")

def search(request):
    title = request.GET.get('query')
    if len(title) > 80:
        query = post.objects.none()
    else:
        querytitle = post.objects.filter(title__icontains=title)
        querycontent = post.objects.filter(content__icontains=title)
        query = querytitle.union(querycontent)
    if query.count() == 0:
        messages.error(request, "No Such result Found!!!")
    return render(request,"home/search.html", {'posts': query, 'title': title})

def signup(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        name = request.POST["name"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["pass1"]
        cpassword = request.POST["pass2"]

        if len(uname) > 15:
            messages.error(request, "Username Must be short")
            return redirect("/")
        if not uname.isalnum():
            messages.error(request, "Username only contain letters and numbers ")
            return redirect("/")
        if password != cpassword:
            messages.error(request, "Both Passwords must be same")
            return redirect("/")

        # Creating User
        myuser = User.objects.create_user(uname, email, password)
        myuser.first_name = name
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect("/")
    else:
        return HttpResponse("404 Not Found")

def loginn(request):
    if request.method == 'POST':
        uname = request.POST['luname']
        password = request.POST['pass']

        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login Successful")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials Please try again!!")
            return redirect("/")
    else:
        return HttpResponse("404 Not Found")

def logoutt(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect("/")