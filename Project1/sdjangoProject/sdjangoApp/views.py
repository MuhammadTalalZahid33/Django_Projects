from django.shortcuts import render

# Create your views here.
def subHome(request):
    return render(request, 'sdjangoApp/index.html')