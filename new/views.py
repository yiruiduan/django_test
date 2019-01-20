from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse

# Create your views here.
def index(request,*args,**kwargs):
    print(request.COOKIES)
    for k,v in request.environ.items():
        print(k,v)
    return HttpResponse("hello world")

def tpl1(request):
    user_list=["yi","rui","duan"]
    return render(request,"new/tpl1.html",{"u":user_list})

def tpl2(request):
    name="root"
    return render(request,"new/tpl2.html",{"name":name})

def tpl3(request):
    status="已删除"
    return render(request,"new/tpl3.html",{"status":status})