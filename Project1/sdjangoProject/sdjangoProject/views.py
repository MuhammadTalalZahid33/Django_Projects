from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("you are at about page")

def contact(request):
    return HttpResponse("Contact Us, You need Us")

