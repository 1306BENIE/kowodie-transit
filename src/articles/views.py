from django.shortcuts import render 
from django.http import HttpResponse

from .models import Article


def articles_view(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", context={'articles': articles})

def article_view(request, slug):
    return HttpResponse('Page article')
