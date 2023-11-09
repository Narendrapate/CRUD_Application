from django.shortcuts import render ,redirect
from app. models import * 
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def ragistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password= make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse('email number already exists')
        elif User.objects.filter(phone=phone).exists():
            return HttpResponse('phone number already exists')
        else:
            User.objects.create(name=name,email=email,phone=phone,password=password)
            return HttpResponse('User Create')

def table(request):
    data = User.objects.all()
    return render(request,"table.html",{"data":data})

def userdelete(request,pk):
    User.objects.get(id=pk).delete()
    return redirect ("/table/")

def update_detials(request,uid):
    persone = User.objects.get(id=uid)
    return render(request,"update.html",{"persone":persone})

def update_view(request):
    if request.method == "POST":
        uid = request.POST['uid']
        name = request.POST['name']
        email = request .POST['email']
        phone = request .POST['phone']
        User.objects.filter(id=uid).update(name=name,email=email,phone=phone)
        return redirect("/table/")
    