from django.shortcuts import render 

from .db_articles import articles 


def articles_view(request):
    # articles = Article.objects.all().order_by('-date_publication')
    return render(request, "articles/list.html", context={'articles': articles})
"""
def article_view(request, slug):
   return HttpResponse("page d'article")
   """