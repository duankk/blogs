from django.contrib import admin
from .models import Article, Tag, Tui, Categoery, Link, Banner

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time', 'modified_time')
    #满50条数据就字段分页
    list_per_page = 50
    #后台数据列表排序方法
    ordering = ('-created_time',)
    #设置哪些字段可以点击进入编辑页面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')
    list_display_links = ('id', 'img')


@admin.register(Categoery)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')