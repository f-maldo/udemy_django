from django.contrib import admin
from .models import Category, Type, Element


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Element, ElementAdmin)
