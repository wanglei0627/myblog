#!/usr/bin/env python3
from django.urls import path
from .views import blog_detail, blog_type,blog_list,blog_with_date

urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('<int:blog_pk>', blog_detail, name='blog_detail'),
    path('type/<int:type_pk>', blog_type, name="blog_type"),
    path('date/<int:year>/<int:month>',blog_with_date,name="blog_with_date"),
]
