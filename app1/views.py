from django.shortcuts import render



def nath(request):
    return render(request,'nath.html')

    
from django.http import HttpResponse


def sri(request):
    return HttpResponse('<center><h1>This is app1 string view')




# Create your views here.
