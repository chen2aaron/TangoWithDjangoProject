# -*- coding:utf-8 -*-
from django.conf.urls import url, patterns
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # 匹配URL斜杠前所有的字母数字
    # 例如 a-z, A-Z, 或者 0-9)和连字符(-
    # 然后把这个值作为category_name_slug参数传递给views.category(),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page, name='add_page'),

)
