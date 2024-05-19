from django.contrib import admin
from .models import DishCategory, Dish

from django.utils.safestring import mark_safe


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'sort','slug')
    list_editable = ('name', 'is_visible', 'sort', 'slug')
    list_filter = ('is_visible',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_scr_tag', 'name', 'is_visible', 'price', 'sort', 'category')
    list_editable = ('name', 'is_visible', 'price', 'sort', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'ingredients')

    def photo_scr_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}', width=50, height=50>")

    photo_scr_tag.short_description = 'Dish photo'