from django.urls import path
from .views import *

urlpatterns = [
    path('', articles, name='articles_url'),
    path('<int:article_id>', article, name='article_url'),
    path('addlike/<int:article_id>', add_like, name='add_like_url'),
    path('addcomment/<int:article_id>', add_comment, name='add_comment_url')
  ]