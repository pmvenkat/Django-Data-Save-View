from django.shortcuts import render
from django.http import HttpResponse
from pages.models import User_Info
# Create your views here.
def index(request):
    return render(request, 'index.html', {'name':'Helloworld'})

def add(request):
    return render(request, 'add.html')

def view(request):
    datas = User_Info.objects.all()
    return render (request,"view.html",{'datas':datas})

def submit(request):
    print("Data Inserted")
    name = request.POST["name"]
    mobile = request.POST["mobile"]
    age = request.POST["age"]
    address = request.POST["address"]

    datainfo = User_Info(name=name,age=age,mobile=mobile,address=address)
    datainfo.save()
    return render(request, 'add.html')

