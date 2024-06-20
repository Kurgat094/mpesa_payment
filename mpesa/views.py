from django.shortcuts import render,redirect

# Create your views here.
def payment(request):
    return render(request,"payment.html")

def home(request):
    return render(request,"index.html")