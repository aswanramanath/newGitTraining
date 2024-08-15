from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View

from django.contrib.auth.models import User

class Home(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        uname=request.POST['user']
        pas=request.POST['passs']
        data=authenticate(request,user=uname,passs=pas)
        if data:
            login(request,data)
            return redirect('details.html')
        else:
            return redirect('reg')
class Reg(View):
    def get(self,request):
        return render(request,'reg.html')
    def post(self,request,*args,**kwargs):
        uname=request.POST['name']
        pas=request.POST['psw']
        data1=User.objects.create_user(name=uname,psw=pas)
        if data1:
           return redirect("")
        else:
            return redirect("login")


# Create your views here.
