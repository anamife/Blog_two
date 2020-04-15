from django.db import models

class Article(models.Model):
	class Meta:
		db_table = 'article'

	article_title = models.CharField(max_length=200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=True)

class Comment(models.Model):
	class Meta:
		db_table = 'comment'

	comment_text = models.TextField(verbose_name='Текст комментария')
	comment_article = models.ForeignKey(Article, on_delete=models.CASCADE) # В базе данных автоматически называется 'comment_article_id'