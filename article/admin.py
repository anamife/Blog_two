from django.contrib import admin
from .models import *

class ArticleInLine(admin.StackedInline):
	model = Comment
	extra = 2 

class ArticleAdmin(admin.ModelAdmin):
	exclude = ['article_likes'] # Не показываем это поле
	inlines = [ArticleInLine] # Можно теперь редактировать и добавлять комментарии
	list_filter = ['article_date'] # Добавляет фильтр


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)