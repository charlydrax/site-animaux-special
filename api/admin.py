from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'display_thumb']
    search_fields = ['name']
    list_filter = ['category']
    list_per_page = 25
    # list_editable = ['status']

    def display_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width:50px;" />', obj.image.url)
        return None
    
    # display_thumb.short_description = 'Thumbnail'
    
admin.site.register(models.Animal, AnimalAdmin)
admin.site.register(models.Category)
admin.site.register(models.Location)
