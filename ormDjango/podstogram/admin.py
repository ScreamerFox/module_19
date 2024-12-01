from django.contrib import admin
from .models import News, Promotion

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published')
    search_fields = ('title', 'content')
    list_filter = ('published',)
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = "Опубликовать"

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name_prom', 'price',)
    search_fields = ('name_prom',)

