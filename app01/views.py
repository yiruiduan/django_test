from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
from app01 import models
import json
# Create your views here.
def login(request):
    return HttpResponse("app01")

class Business(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(Business,self).dispatch(request,*args,**kwargs)
        return result
    def get(self,request,*args,**kwargs):
        group_list=models.Host_Group.objects.all()
        app_list = models.Application.objects.all()
        return render(request,"host/index.html",{"status":"hide","group_list":group_list,"app_list":app_list})


class Host_list(View):
    def dispatch(self, request, *args, **kwargs):
        result=super(Host_list,self).dispatch(request,*args,**kwargs)
        return result
    def get(self,request,*args,**kwargs):
        host_list=models.Host_List.objects.filter(host_group_id=kwargs["nid"])
        group_list = models.Host_Group.objects.all()
        app_list=models.Application.objects.all()
        return render(request,"host/index.html",{"status":"hide","group_list":group_list,"host_list":host_list,"app_list":app_list})



def detail(request,*args,**kwargs):
    host_info=models.Host_Process.objects.filter(process_in_host_id=kwargs["nid"])
    group_list = models.Host_Group.objects.all()
    return render(request,"host/detail.html",{"group_list":group_list,"host_info":host_info})

def test_ajax(request):
    try:
        ret={"status":True,"error":None,"data":None}
        hostname=request.POST.get("host_name",None)
        hostip=request.POST.get("host_ip",None)
        hostport=request.POST.get("host_port",None)
        hostuser=request.POST.get("host_user",None)
        hostingroup=request.POST.get("host_in_group",None)
        hostid=request.POST.get("host_id",None)
        host_in_app=request.POST.getlist("host_in_app",None)
        if hostid:
            # print(request.POST)
            models.Host_List.objects.filter(nid=hostid).update(
                host_name=hostname,
                host_ip=hostip,
                host_port=hostport,
                host_user=hostuser,
                host_group_id=hostingroup
            )
        else:
            if hostname and hostip and hostport and hostuser and hostingroup:
                obj=models.Host_List.objects.create(
                    host_name=hostname,
                    host_ip=hostip,
                    host_port=hostport,
                    host_user=hostuser,
                    host_group_id=hostingroup
                )
                print(obj)
                if host_in_app:
                    hostid=obj.nid
                    print(hostid)
                    for app in host_in_app:
                        app_obj=models.Application.objects.get(id=app)
                        app_obj.r.add(hostid)

            else:
                ret["status"]=False
                ret["error"]="有空项"
    except Exception as e:
        ret["status"]=False
        ret["error"]="服务错误"
        print("数据库操作有误")
    return HttpResponse(json.dumps(ret))

def app(request):
    app_list=models.Application.objects.all()
    return render(request,"host/app.html",{"app_list":app_list})
