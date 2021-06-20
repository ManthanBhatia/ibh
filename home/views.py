from django.shortcuts import render, HttpResponse, redirect
from datetime import date, datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

from home.models import Suggestion
from home.models import Query
from home.models import Thoughts
from home.models import Regngo
from home.models import Regres1
from home.models import Volunteer

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about_us.html')

def services(request):
    return render(request, 'services.html')    

def contact(request):
    return render(request, 'Contact Us.html')

def donation(request):
    return render(request, 'donation_page.html')    
def query(request):
    if request.method=="POST":
        email = request.POST.get('email')
        name=request.POST.get('name')
        comment = request.POST.get('comment')
        query= Query(name=name, email=email, comment=comment, date=datetime.today())
        query.save()
        messages.success(request, 'Your query has been sent. You will be responded in 24 hours over mail.')

    return render(request, 'query_page.html') 
def regngo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pocname=request.POST.get('pocname')
        email = request.POST.get('email')
        city=request.POST.get('city')
        state = request.POST.get('state')
        pincode=request.POST.get('pincode')
        address=request.POST.get('address')
        number=request.POST.get('number')
        regngo= Regngo(name=name,pocname=pocname, email=email, city=city, state=state, pincode=pincode, address=address, number=number, date=datetime.today())
        regngo.save()
        messages.success(request, 'Thank You. Your NGO has been registered')

    return render(request, 'register_ngo.html')
def regres(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pocname=request.POST.get('pocname')
        email = request.POST.get('email')
        regnum =request.POST.get('regnum')
        state = request.POST.get('state')
        pincode=request.POST.get('pincode')
        address=request.POST.get('address')
        number=request.POST.get('number')
        regres= Regres1(name=name,pocname=pocname, email=email, regnum=regnum, state=state, pincode=pincode, address=address, number=number, date=datetime.today())
        regres.save()
        messages.success(request, 'Thank You. Your details have been received. Your account will be verified within 24 hours and the login credentials would be sent over an email.')
    return render(request, 'register_restraunt.html') 
def suggestion(request):
    if request.method=="POST":
        email = request.POST.get('email')
        name=request.POST.get('name')
        vsug = request.POST.get('vsug')
        suggestion= Suggestion(name=name, email=email, vsug=vsug, date=datetime.today())
        suggestion.save()
        messages.success(request, 'Your suggestion has been sent')

    return render(request, 'suggestion_page.html') 
def signup(request):
    return render(request, 'sign_up.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")     
def blogs(request):
    return render(request, 'Blogs.html')  
def thoughts(request):
    if request.method=="POST":
        email = request.POST.get('email')
        name=request.POST.get('name')
        thought = request.POST.get('thought')
        thoughts= Thoughts(name=name, email=email, thought=thought, date=datetime.today())
        thoughts.save()
        messages.success(request, 'Thank You. Your thoughts have been submitted')

    return render(request, 'Thoughts.html')                       
def index12(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index12.html')
def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect("/index12")
        else:
           messages .error(request, "Invalid Credentials, please try again")
           return render(request, 'login.html') 

    return render(request, 'login.html')

def volunteer(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        address=request.POST.get('address')
        number=request.POST.get('number')
        volunteer= Volunteer(name=name, email=email, address=address, number=number, date=datetime.today())
        volunteer.save()
        messages.success(request, 'Thank You. Your details have been received. You will be contacted soon')
    return render(request, 'volunteer.html')