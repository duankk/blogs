from django.shortcuts import render
from django.http import HttpResponse


from .models import Article
# Create your views here.

def index(request):
    sitename = 'Django中文网'
    url = 'www.django.cn'
    lists = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    mydict = {
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }

    allArticle = Article.objects.all()

    context = {
        'sitename': sitename,
        'url': url,
        'lists': lists,
        'mydict': mydict,
        'allArticle': allArticle,
    }


    return render(request, 'index.html', context)
