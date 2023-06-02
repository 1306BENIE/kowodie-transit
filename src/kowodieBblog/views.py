from django.shortcuts import render 
from django.http import HttpResponse
from .db_articles import articles

def home_view(request): 
    return render(request, "home.html")

def contact_view(request):
    return render(request, "contact.html")


def article_view(request):
    return render(request, "article.html", context={'articles': articles})