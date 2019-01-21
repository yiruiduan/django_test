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
for i in range(1009):
    USER_LIST.append(i)
def user_list(request):
    per_num=10
    mark_per_page = 11

    page_num=request.GET.get("p","1")
    page_num=int(page_num)
    start_num=(page_num-1)*per_num
    end_num=page_num*per_num
    user=USER_LIST[start_num:end_num]
    user_total=len(USER_LIST)
    total_count,y=divmod(user_total,per_num)
    if y:
        total_count+=1
    page_str=[]
    # 上一页
    if page_num <=1:
        prev= '<a class="page_sty" href="javascript:void(0)">上一页</a>'
    else:
        prev = '<a class="page_sty" href="/new/user_list?p=%s">上一页</a>'%(page_num-1)
    page_str.append(prev)

    # 显示的页签
    if total_count <= mark_per_page:
        start_index = 1
        end_index = total_count +1
    else:
        if page_num <= (mark_per_page+1)/2 :
            start_index = 1
            end_index = 11
        else:
            if page_num+(mark_per_page+1)/2 > total_count:
                end_index= total_count+1
                start_index= total_count -11 +1
            else:
                start_index = page_num - (mark_per_page -1)/2
                end_index = page_num +(mark_per_page +1)/2

    for i in range(int(start_index),int(end_index)):
        if i == int(page_num):
            tmep='<a class="page_sty active" href="/new/user_list?p=%s">%s</a>' %(i,i)
        else:
            tmep='<a class="page_sty" href="/new/user_list?p=%s">%s</a>' %(i,i)
        page_str.append(tmep)
    # 下一页
    if page_num >= total_count:
        nex= '<a class="page_sty" href="javascript:void(0)">下一页</a>'
    else:
        nex= '<a class="page_sty" href="/new/user_list?p=%s">下一页</a>'%(page_num+1)
    page_str.append(nex)
    # 跳转
    jump ="""
        <input style="width: 28px;height: 28px;border-radius: 5px" type="text"/><a class="page_sty" onclick="jumpTo(this,'new/user_list?p=');" id="jump_to">跳转到</a>
        <script>
            function jumpTo(ths,base) {
                var max_page = %d;
                var val=document.getElementById("jump_to").previousSibling.value;
                if( val > max_page){
                    val =max_page;
                };
                if (val < 1){val =1};
                location.href = base+ val;
            }
        </script>    """ %total_count
    page_str.append(jump)
    page_str="".join(page_str)
    page_str=mark_safe(page_str)
    return render(request,"new/user_list.html",{"li":user,"page_str":page_str})