from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    # return HttpResponse(<h3>"Welcome to the Home Page!"</h3>)
    return render(request, "home.html")
