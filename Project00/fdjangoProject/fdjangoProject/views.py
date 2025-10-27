from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, you are at Home page so make yourself at home....")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("You are at about us page")

def contact(request):
    return HttpResponse("Now, at contact us page")