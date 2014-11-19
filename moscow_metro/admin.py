# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MetroLine, Metro


# try to use sortable stacked inline from django-suit
try:
    from suit.admin import SortableStackedInline
    class StackedAdmin(SortableStackedInline): pass
except ImportError:
    class StackedAdmin(admin.StackedInline): pass


class MetroAdminInline(StackedAdmin):
    model = Metro
    extra = 0
    list_display = ('title', 'line', )
    list_display_links = ('title', )
    list_filter = ('title', 'line')
    search_fields = ('title', )


class MetroLineAdmin(admin.ModelAdmin):
    inlines = [MetroAdminInline, ]
    list_display = ('number', 'title', 'get_admin_color')
    list_display_links = ('number', 'title', 'get_admin_color')
    list_filter = ('number', 'title')
    search_fields = ('number', 'title')


admin.site.register(MetroLine, MetroLineAdmin)
