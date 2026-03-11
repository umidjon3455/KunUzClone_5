from .models import Contact, News, Category
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)

# Register your models here.
# 1-usul
# admin.site.register(News)
# admin.site.register(Category)

# 2-usul
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']



