from django.contrib import admin
from pradact.models import Pradact, Category, Tag
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(Pradact)
class PradactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'category', 
        'get_image',
        'is_published' ,
    )
    list_display_links = ('id', 'name')

    search_fields = (
        'name', 
        'tags__name', 
        'category__name',
    )
    list_editable = ('is_published',)
    list_filter = ('tags','is_published', 'category',)

    readonly_fields = (
        'get_full_image',
    )


    @admin.display(description='Изображение')
    def get_image(self, instance: Pradact):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="100px">')
        return '-'
    
    @admin.display(description='Изображение')
    def get_full_image(self, instance: Pradact):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="50%">')
        return '-'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

