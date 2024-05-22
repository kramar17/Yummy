from django.contrib import admin
from .models import DishCategory, Dish, Gallery, Reservation, EventsImage, Staff

from django.utils.safestring import mark_safe


admin.site.register(Gallery)
admin.site.register(Reservation)


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
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}', width=50, height=50>")

    photo_scr_tag.short_description = 'Dish photo'


@admin.register(EventsImage)
class EventsImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'is_visible', 'photo_scr_tag')
    list_editable = ('description', 'price', 'is_visible',)
    search_fields = ('name',)

    def photo_scr_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}', width=80, height=80>")

    photo_scr_tag.short_description = 'Event photo'


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'position', 'photo_scr_tag')
    list_editable = ('name', 'is_visible', 'position')
    search_fields = ('name',)

    def photo_scr_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}', width=50, height=50>")

    photo_scr_tag.short_description = 'Staff photo'
