# -*- coding:utf-8 -*-
from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='请输入类型名称')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # inline类 给表单提供额外的信息
    class Meta:
        # 关联 ModelFrom 和 一个model
        model = Category
        # Django1.7+需要通过fields指定包含的字段,或者通过exclude指定排除的字段.
        fields = ('name', 'views')


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='请输入标题')
    url = forms.URLField(max_length=200, help_text='请输入链接')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # 隐藏了ForeignKey 排除了category
        exclude = ('category',)
        # 或者这样写
        # fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # 如果url是空的或者不包含http://头 就自动加上
        if url and not url.startwith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
