from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def practice(request):
    return render(request,"pybo/index.html")
def first_practice(request):
    return render(request,"pybo/1.html")
def second_practice(request):
    return render(request,"pybo/2.html")
def third_practice(request):
    return render(request,"pybo/3.html")
