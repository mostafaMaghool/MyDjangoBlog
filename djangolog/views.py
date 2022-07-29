from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # return HttpResponse('HOME i am')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>Hi, how are you<h1>')
    return render(request, 'about.html')

