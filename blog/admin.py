from django.contrib import admin
from .models import BlogType, Blog, Comment


# Register your models here.


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type_name",
    )
    ordering = ("-id",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "title",
        "tag",
        "author",
        "get_read_num",
        "create_time",
        "update_time",
    )
    ordering = ("-id",)
    # get_user_article.short_description =


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'blog',
        'user_comment',
        'content',
        "create_time",
        "update_time",

    )
