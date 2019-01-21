from  django.utils.safestring import mark_safe
class Page(object):
    def __init__(self,page_num,data_total,data_per_page=10,mark_per_page=11):
        self.page_num=page_num
        self.data_per_page=data_per_page
        self.mark_per_page=mark_per_page
        self.data_total=data_total
    @property
    # 根据当前的页号   算出数据切片的起始位置
    def start(self):
        return (self.page_num-1)*self.data_per_page
    @property
    # 根据当前的页号   算出数据切片的终止位置
    def end(self):
        return self.page_num*self.data_per_page
    @property
    # 总共生成多少页，通过总数据和每页多少数据
    def total_count(self):
        total_count, y = divmod(self.data_total, self.data_per_page)
        if y:
            total_count += 1
        return total_count
    # 页码的a标签
    def page_str(self,base_url):
        page_str = []
        # 上一页
        if self.page_num <= 1:
            prev = '<a class="page_sty" href="javascript:void(0)">上一页</a>'
        else:
            prev = '<a class="page_sty" href="/new/user_list?p=%s">上一页</a>' % (self.page_num - 1)
        page_str.append(prev)

        # 显示的页签
        if self.total_count <= self.mark_per_page:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.page_num <= (self.mark_per_page + 1) / 2:
                start_index = 1
                end_index = 11
            else:
                if self.page_num + (self.mark_per_page + 1) / 2 > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - 11 + 1
                else:
                    start_index = self.page_num - (self.mark_per_page - 1) / 2
                    end_index = self.page_num + (self.mark_per_page + 1) / 2

        for i in range(int(start_index), int(end_index)):
            if i == int(self.page_num):
                tmep = '<a class="page_sty active" href="%s?p=%s">%s</a>' % (base_url,i, i)
            else:
                tmep = '<a class="page_sty" href="%s?p=%s">%s</a>' % (base_url,i, i)
            page_str.append(tmep)
        # 下一页
        if self.page_num >= self.total_count:
            nex = '<a class="page_sty" href="javascript:void(0)">下一页</a>'
        else:
            nex = '<a class="page_sty" href="%s?p=%s">下一页</a>' % (base_url,self.page_num + 1)
        page_str.append(nex)
        # 跳转
        jump = """
            <input style="width: 28px;height: 28px;border-radius: 5px" type="text"/><a class="page_sty" onclick="jumpTo(this,'%s?p=');" id="jump_to">跳转到</a>
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
            </script>    """ % (base_url,self.total_count)
        page_str.append(jump)
        page_str = "".join(page_str)
        page_str = mark_safe(page_str)
        return page_str