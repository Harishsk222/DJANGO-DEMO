from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Banglore,Mumbai,Chennai

#factories Banglore
def home2(request):
    mymembers = Banglore.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'home2.html',d)


def home(request):
    return render(request,'home.html')


# Display Stack Data
def Banglore_list(request):
    mymembers = Banglore.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'banglore_list.html',d)

# Adding Daily Update Stack Banglore factory

def add_report(request):
    if request.method=="POST":
      date = request.POST["date"]
      bl1 = int(request.POST['bl1'])
      bl2 =int(request.POST['bl2'])
      bl3 = int(request.POST['bl3'])
      bl4 = int(request.POST['bl4'])
      bl5 = int(request.POST['bl5'])
      stock = Banglore(Date=date, Bl1=bl1,Bl2=bl2,Bl3=bl3,Bl4=bl4,Bl5=bl5)
      stock.save()
      print("sussfull")
      return redirect('home2')

    return render(request,'add_report.html')





#___________________________________________________________________________________________


def Mumbai_list(request):
    mymembers = Mumbai.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'mumbai_list.html',d)


def home3(request):
    mymembers = Mumbai.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'home3.html',d)


def madd_report(request):
  if request.method=="POST":
    date = request.POST["date"]
    ml1 = int(request.POST['bl1'])
    ml2 =int(request.POST['bl2'])
    ml3 = int(request.POST['bl3'])
    ml4 = int(request.POST['bl4'])
    
    stock = Mumbai(Date=date, Ml1=ml1,Ml2=ml2,Ml3=ml3,Ml4=ml4)
    stock.save()
    print("sussfull")
    return redirect('home3')

  return render(request,'madd_report.html')



  #___________________________________________________________________________________________


def home4(request):
    mymembers = Chennai.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'home4.html',d)



def cadd_report(request):
  if request.method=="POST":
    date = request.POST["date"]
    cl1 = int(request.POST['bl1'])
    cl2 =int(request.POST['bl2'])
    cl3 = int(request.POST['bl3'])
    
    stock = Chennai(Date=date, Cl1=cl1,Cl2=cl2,Cl3=cl3)
    stock.save()
    print("sussfull")
    return redirect('home4')

  return render(request,'cadd_report.html')

  
def chennai_list(request):
    mymembers = Chennai.objects.all()
    d={'data':mymembers}
    print(d)
    return render(request,'chennai_list.html',d)