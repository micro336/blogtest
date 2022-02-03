from django.db import models # 每个类都要继承models.Model
from django.contrib.auth.models import User #django内置应用 专门处理网站用户的注册、登录等流程
from  django.utils import timezone
from  django.urls import reverse


class Category(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name = '分类'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


class Tag(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name = '标签'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


class Post(models.Model):
  title = models.CharField('标题',max_length=100)

  body = models.TextField('正文')

  created_time = models.DateTimeField('创建时间',default=timezone.now)
  modified_time = models.DateTimeField('修改时间')


  expert = models.CharField('摘要',max_length=200, blank=True)

  category = models.ForeignKey(Category,verbose_name='分类', on_delete=models.CASCADE)#一对多
  tags = models.ManyToManyField(Tag,verbose_name='标签', blank=True)#多对多

  author = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)

  def __str__(self):
    return self.title


  # 自定义 get_absolute_url 方法
  # 记得从 django.urls 中导入 reverse 函数
  def get_absolute_url(self):
    return reverse('blog:detail', kwargs={'pk': self.pk})
  def get_absolute_url2(self):
    return reverse('blog:index')

  class Meta:
    verbose_name = '文章'
    verbose_name_plural = verbose_name

    def __str__(self):
      return self.title
  # ？？？
  def save(self, *args, **kwargs):
    self.modified_time = timezone.now()
    super().save(*args, **kwargs)
