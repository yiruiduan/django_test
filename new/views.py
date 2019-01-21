from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from utils import pagination
from new import models
# Create your views here.
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get("username")
        if not v:
            return redirect("/new/login.html")
        return func(request,*args,**kwargs)
    return inner

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

def tpl4(request):
    status="已删除"
    return render(request,"new/tpl4.html")

USER_LIST=[]
for i in range(1009):
    USER_LIST.append(i)

@auth
def user_list(request):
    page_num=request.GET.get("p","1")
    page_num=int(page_num)
    data_per_page=request.COOKIES.get("data_per_page",10)
    data_per_page=int(data_per_page)
    print(data_per_page)
    page_obj=pagination.Page(page_num,len(USER_LIST),data_per_page)
    user=USER_LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/new/user_list")
    return render(request,"new/user_list.html",{"li":user,"page_str":page_str})



############################cookie##################################



def login(request):
    if request.method == "GET":
        return render(request,"new/login.html")
    if request.method =="POST":
        u= request.POST.get("user",None)
        p=request.POST.get("password",None)
        auto=request.POST.get("login_auto")
        print(u,p,auto)
        user_exist=models.NewUserInfo.objects.filter(user_name=u,user_pwd=p).first()
        if user_exist:
            res =redirect("/new/index")
            if auto:
                print("长时间")
                res.set_signed_cookie("username",u,max_age=3)
                res.set_cookie("user_type","dog",httponly=True,max_age=3)
            else:
                print("短时间")
                res.set_signed_cookie("username",u)

            return res
        else:
            return render(request,"new/login.html",{"error_msg":"用户名密码错误"})

@auth
def index(request):
    #获取当前已经登录的用户
    v=request.COOKIES.get("username")
    return render(request,"new/index.html",{"current_user":v})





