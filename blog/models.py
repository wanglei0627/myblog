from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNum


# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(verbose_name="分类", max_length=30)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="作者")
    tag = models.ForeignKey(
        BlogType, verbose_name="标签", on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create_time',)

    def get_read_num(self):
        try:
            content_type = ContentType.objects.get_for_model(Blog)
            readnum = ReadNum.objects.get(content_type=content_type, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.DO_NOTHING,verbose_name='关联',related_name='blog')
    user_comment=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='用户信息')
    content=models.TextField(max_length=150,verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    def __str__(self):
        return self. content
    class Meta:
        ordering=("-create_time",)