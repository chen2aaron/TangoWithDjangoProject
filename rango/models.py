# -*- coding:utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """
        页面的类名 浏览量 点赞数
        slug 将图书分类的名称用做url后缀（空格用-替换）
    """
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    """
        页面属于那一类 题目 链接 浏览量
    """
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
