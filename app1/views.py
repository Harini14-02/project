from django.shortcuts import render, redirect


def home(request):
    return render(request,"app1/home.html")
def home1(request):
    return render(request,'app1/home1.html')

