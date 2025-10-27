from django.shortcuts import render

# Create your views here.
def firapp(request):
    return render(request, 'fdjangoApp/index.html')
