from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings

def blog_list(request):
    blog_list_all = Blog.objects.all()
    paginator = Paginator(blog_list_all,settings.EACH_PAGE_BLOGS_NUM)#每页显示4篇博客
    page_num = request.GET.get('page')#get the page arg,if not exist use the default value 1
    page_of_blogs = paginator.get_page(page_num)#get_page把字符串转为数字,如果超过页码范围默认为1,django支持的
    current_num = page_of_blogs.number#获取当前页码
    max_page_num = paginator.num_pages#获取最大页码
    #获取当前页前后范围2以内的页码数(第一页和最后一页要特殊处理)
    page_range = [ i for i in range(current_num-2,current_num+3) if i>0 and i<=max_page_num]
    #增加省略号,重点了解
    if page_range[0]-1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1] >=2:
        page_range.append('...')
    #增加首页和尾页
    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context['page_range'] = page_range
    context['page_of_blogs'] = page_of_blogs
    context['blogs'] = page_of_blogs.object_list
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)
    
def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)
    
def blogs_with_type(request,blogs_with_type):
    blog_type = get_object_or_404(BlogType,pk=blogs_with_type)
    blog_list_all = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blog_list_all,settings.EACH_PAGE_BLOGS_NUM)#每页显示4篇博客
    page_num = request.GET.get('page')#get the page arg,if not exist use the default value 1
    page_of_blogs = paginator.get_page(page_num)#get_page把字符串转为数字,如果超过页码范围默认为1,django支持的
    current_num = page_of_blogs.number#获取当前页码
    max_page_num = paginator.num_pages#获取最大页码
    #获取当前页前后范围2以内的页码数(第一页和最后一页要特殊处理)
    page_range = [ i for i in range(current_num-2,current_num+3) if i>0 and i<=max_page_num]
    #增加省略号,重点了解
    if page_range[0]-1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1] >=2:
        page_range.append('...')
    #增加首页和尾页
    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context['page_range'] = page_range
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html',context)