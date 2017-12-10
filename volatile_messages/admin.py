from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_level_display', 'get_preview')
    list_filter = ('level',)
    ordering = ('title',)
    prepopulated_fields = {'title': ('content', )}
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                ('title', 'level'),
                ('content', 'template_name'),
                'read_by',
            )
        }),
    )
