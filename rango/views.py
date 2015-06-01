# -*- coding:utf-8 -*-
from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


def index(request):
    # 访问数据库中category，对likes进行降序排列，取出前5
    category_list = Category.objects.order_by('-likes')[:5]
    # 访问结束后，把这个前五的list传递给context_dict
    context_dict = {'categories': category_list}
    # 将dict作为参数 render 给 templates
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_slug):
    # 定义一个字典，从models里面导入数据
    context_dict = {}
    try:
        # 通过参数category_name_slug的值来决定是哪个目录
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # 检索所有关联的pages
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    # 是POST 方法吗？
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # 提供了有效的表单吗？
        if form.is_valid():
            # 将表单存入数据库
            form.save(commit=True)
            return index(request)
        else:
            # 终端打印错误
            print form.errors

    else:
        # 如果是GET方法 就展示表单
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    return render(request, 'rango/add_page.html', {'form': form, 'category': cat})
