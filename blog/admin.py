from django.contrib import admin
from .models import BlogType,Blog
# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title','blog_type','author','created_time','last_updated_time')