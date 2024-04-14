from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.


def index(request):
    return render(request, "index.html")


def users(request):
    return render(request, "users.html")


def datathrow(request):
    return render(request, "datathrow.html")


def datacatch(request):
    message = request.GET.get("message")
    # 만약에 message가 없더라도 일단 뜨게 할 수 있음.
    context = {
        "data": message,
    }
    return render(request, "datacatch.html", context)


def articles(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)


def new(request):
    return render(request, "new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    article = Article(title=title, content=content)
    article.save()
    context = {
        "article": article,
    }
    return render(request, "create.html", context)
