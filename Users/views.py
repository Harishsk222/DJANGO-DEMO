from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


# user Login Method
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        select = int(request.POST['select'])

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            if select==1 and username=="Delhi":
                 return redirect("home")
            elif select==2 and username=="Banglore":
                return redirect("home2")   
            
            elif select ==3 and username=="Mumbai":
                return redirect("home3")
            elif select ==4 and username=="Chennai":
                return redirect("home4") 
            else:  
                messages.info(request,'invalid credentials')
        else:
            messages.info(request,'invalid credentials')

    
    return render(request,'login.html')    
   
# User Logout Method
def logout(request):
    auth.logout(request)
    return redirect('login')       
    #return render(request,'login.html')
