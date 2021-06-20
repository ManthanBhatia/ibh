
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("blogs", views.blogs, name='blogs'),
    path("donation", views.donation, name='donation'),
    path("query", views.query, name='query'),
    path("regngo", views.regngo, name='regngo'),
    path("regres", views.regres, name='regres'),
    path("suggestion", views.suggestion, name='suggestion'),
    path("signup", views.signup, name='signup'),
    path("thoughts", views.thoughts, name='thoughts'),
    path("logout", views.logoutuser, name="logout"),
    path("login", views.loginuser, name="login"),
    path("index12", views.index12, name="index12"),
    path("volunteer", views.volunteer, name="volunteer")


]