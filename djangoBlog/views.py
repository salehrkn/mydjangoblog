from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    #return HttpResponse('Hi There! Im Hello World')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('HOME')
    return render(request, 'Home.html')

