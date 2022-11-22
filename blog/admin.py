from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tag',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('username',)


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(About, AboutAdmin)
admin.site.register(Profession)

