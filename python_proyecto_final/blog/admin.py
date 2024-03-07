from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author__username')
    list_filter = ('date', 'author')

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'body', 'author', 'date', 'image')
        }),
    )
