from django.contrib import admin
from .models import Content, Category

# Register your models here.


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'status']
    search_fields = ('slug', 'created')
    # prepopulated_fields = {"slug": ('title',)}


admin.site.register(Content, ContentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'status']
    search_fields = ('slug', 'created')


admin.site.register(Category, CategoryAdmin)
