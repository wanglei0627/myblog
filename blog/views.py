from django.shortcuts import render, get_object_or_404
from django.conf import settings
from read_statistics.models import ReadNum
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Count

from .models import BlogType, Blog, Comment



# Create your views here.
def get_blog_paginator(request, blog_all_list):
    paginator = Paginator(blog_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 分页
    pag_num = request.GET.get('page', 1)  # 获取页码请求
    pag_of_blog = paginator.get_page(pag_num)
    blog_dates = Blog.objects.dates('create_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(
            create_time__year=blog_date.year, create_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context["contents"] = pag_of_blog
    context["types"] = BlogType.objects.annotate(
        blog_count=Count('blog'))  # 获取blog类型分档数量
    context['blog_dates'] = blog_dates_dict
    return context


#
def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    if not request.COOKIES.get('blog_%s_read' % blog_pk):
        content_type = ContentType.objects.get_for_model(Blog)
        if ReadNum.objects.filter(content_type=content_type, object_id=blog_pk).count():
            readnum = ReadNum.objects.get(content_type=content_type, object_id=blog_pk)
        else:
            readnum = ReadNum(content_type=content_type, object_id=blog_pk)
        readnum.read_num += 1
        readnum.save()

    context["content"] = blog
    context["previous_page"] = Blog.objects.filter(
        create_time__gt=blog.create_time).last()
    context["next_page"] = Blog.objects.filter(
        create_time__lt=blog.create_time).first()

    blog_comment = Comment.objects.filter(blog__id=blog_pk)

    if blog_comment:
        context['comment'] = blog_comment
    else:
        context['comment'] = []

    print(context)

    response = render(request, "blog/article.html", context)
    # 设置访问cookie
    response.set_cookie('blog_%s_read' % blog_pk, 'true', )
    return response


def blog_list(request):
    blog_all_list = Blog.objects.all()
    context = get_blog_paginator(request, blog_all_list)
    return render(request, "blog/articles.html", context)


def blog_type(request, type_pk):
    type_list = get_object_or_404(BlogType, pk=type_pk)  # 判断标签是否存在
    blog_all_list = Blog.objects.filter(tag=type_list)
    context = get_blog_paginator(request, blog_all_list)
    context["type"] = type_list
    return render(request, "blog/type_name.html", context)


def blog_with_date(request, year, month):
    blog_all_list = Blog.objects.filter(
        create_time__year=year, create_time__month=month)
    context = get_blog_paginator(request, blog_all_list)
    context['blog_with_date'] = '%s年%s月' % (year, month)
    return render(request, "blog/blog_with_date.html", context)

def comment(request,blog_pk):
    Comment.objects.filter(blog__id=blog_pk)
