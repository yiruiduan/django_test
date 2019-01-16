from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
from  cmdb import models
# 用户列表
def index(request,*args,**kwargs):
    result = models.UserInfo.objects.all()
    return render(request, "index.html", {"user_list":result, "status": "hide"})
# 用户详情
def detail(request,*args,**kwargs):
    result=models.UserInfo.objects.filter(id= kwargs["id"] )
    # print(result.query)
    return render(request,"detail.html",{"user_info":result})

# 删除用户
def user_delete(request,*args,**kwargs):
    user_info=models.UserInfo.objects.filter(id=kwargs["id"]).delete()
    return redirect("/cmdb/index.html")

# 用户的编辑
# def user_edit(request,*args,**kwargs):
#     if request.method == "GET":
#         result = models.UserInfo.objects.filter(id=kwargs["id"])
#         group_result=models.UserGroup.objects.all()
#         return render(request,"user_edit.html",{"user_info":result,"group_info":group_result})
#     if request.method == "POST":
#         user = request.POST.get("user", None)
#         password = request.POST.get("password", None)
#         tel = request.POST.get("telphone", None)
#         email = request.POST.get("email", None)
#         gender=request.POST.get("gender",None)
#         group_id=request.POST.get("group_id",None)
#         models.UserInfo.objects.filter(id=kwargs["id"]).update(user_name=user,
#                                                                user_pwd=password,
#                                                                user_tel=tel,
#                                                                user_email=email,
#                                                                user_gender=gender,
#                                                                user_group_id=group_id)
#         return redirect("/cmdb/index.html")
def user_edit(request,*args,**kwargs):
    if request.method == "GET":
        user_list=models.UserInfo.objects.all()
        user_info = models.UserInfo.objects.filter(id=kwargs["id"])
        group_result=models.UserGroup.objects.all()
        return render(request, "host/index.html", {"user_list":user_list, "user_info":user_info, "group_info":group_result, "status": ""})
    if request.method == "POST":
        user = request.POST.get("user", None)
        password = request.POST.get("password", None)
        tel = request.POST.get("telphone", None)
        email = request.POST.get("email", None)
        gender=request.POST.get("gender",None)
        group_id=request.POST.get("group_id",None)
        models.UserInfo.objects.filter(id=kwargs["id"]).update(user_name=user,
                                                               user_pwd=password,
                                                               user_tel=tel,
                                                               user_email=email,
                                                               user_gender=gender,
                                                               user_group_id=group_id)
        return redirect("/cmdb/index.html")
# 登录界面
def login(request):
    if request.method =="GET":
        return render(request,"login.html")

def orm(request,status,**kwargs):
    if status == "insert":
        if request.method == "POST":
            user=request.POST.get("user",None)
            password=request.POST.get("password",None)
            tel=request.POST.get("telphone",None)
            email=request.POST.get("email",None)
            models.UserInfo.objects.create(
                user_name=user,
                user_pwd=password,
                user_tel=tel,
                user_email=email
            )
            return render(request,"login.html")
        return render(request,"regist.html")
    elif status == "login":
        if request.method == "POST":
            user=request.POST.get("user",None)
            password=request.POST.get("password",None)
            user_info=models.UserInfo.objects.filter(user_name=user,user_pwd=password).first()
            if user_info:
                print(user_info)
                return redirect("/cmdb/index.html")
            else:
                return render(request,"login.html",{"error_msg":"用户名密码错误"})
    else:
        return render(request,"error.html")

class Home(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(Home,self).dispatch(request,*args,**kwargs)
        return result
    def get(self,request,*args,**kwargs):
        print(args)
        return render(request,"home.html")
    def post(self, request,*args,**kwargs):
        return render(request,"home.html")
