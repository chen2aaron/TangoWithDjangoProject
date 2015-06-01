from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):

    '''
        Admin View for Page
    '''
    list_display = ('title', 'category', 'url')
    # search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):

    '''
        Admin View for Category
    '''
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
