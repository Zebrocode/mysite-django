from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator

def blog_list(request):
    blog_list_all = Blog.objects.all()
    paginator = Paginator(blog_list_all,10)
    page_num = request.GET.get('page')#get the page arg,if not exist use the default value 1
    page_of_blogs = paginator.get_page(page_num)#get_page把字符串转为数字,如果超过页码范围默认为1,django支持的
    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)
    
def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)
    
def blogs_with_type(request,blogs_with_type):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blogs_with_type)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html',context)