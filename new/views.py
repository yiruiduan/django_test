from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

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

def tpl4(request):
    status="已删除"
    return render(request,"new/tpl4.html")

USER_LIST=[]
for i in range(101):
    USER_LIST.append(i)
def user_list(request):
    arg_num=20
    page_num=request.GET.get("p","1")
    page_num=int(page_num)
    start_num=(page_num-1)*arg_num
    end_num=page_num*arg_num
    user=USER_LIST[start_num:end_num]
    user_total=len(USER_LIST)
    count,y=divmod(user_total,arg_num)
    if y:
        count+=1
    page_str=[]
    for i in range(1,count+1):
        if i == int(page_num):
            tmep='<a class="page_sty active" href="/new/user_list/?p=%s">%s</a>' %(i,i)
        else:
            tmep='<a class="page_sty" href="/new/user_list/?p=%s">%s</a>' %(i,i)
        page_str.append(tmep)
    page_str="".join(page_str)
    page_str=mark_safe(page_str)
    return render(request,"new/user_list.html",{"li":user,"page_str":page_str})