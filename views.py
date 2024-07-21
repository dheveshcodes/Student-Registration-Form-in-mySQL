from django.shortcuts import render
from zeta.models import STUDENTS
# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        abc = STUDENTS(Name=name, Email=email, Phone=phone)
        abc.save()
    return render(request,"register.html")