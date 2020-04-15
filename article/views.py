from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.contrib import auth # работа с пользователями


def basic_one(request):
	return render(request, 'myview.html')

def articles(request):
	articles = Article.objects.all()	
	return render(request, 'articles.html', {'articles':articles, 'username':auth.get_user(request).username})

def article(request, article_id=1):
	comment_form = CommentForm
	args = {}
	args['article'] = Article.objects.get(id=article_id)
	args['comments'] = Comment.objects.filter(comment_article_id=article_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render(request, 'article.html', context=args) 

def add_like(request, article_id):
	try:
		article = Article.objects.get(id=article_id)
		article.article_likes += 1
		article.save()
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')

def add_comment(request, article_id):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False) # Запрещаем автоматическое сохранение формы
			comment.comment_article = Article.objects.get(id=article_id)
			form.save()
			return redirect('/'+str(article_id))




