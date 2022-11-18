from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse as HR
# Create your views here.
def index(request):
    #crear página propia o pasar a dmin
    return redirect("/admin")