from django.shortcuts import render, redirect
from .models import Article


# def index(request):
#     return render(request, 'board/index.html')


# Form
def new_article(request):
    return render(request, 'board/new_article.html')


# SAVE new article
def create_article(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect(f'/board/{article.id}')


# Read all
def article_list(request):  # 전체 article 조회하기.
    articles = Article.objects.all()   # []
    return render(request, 'board/article_list.html', {
        'articles': articles
    })


# Read one
def article_detail(request, article_id):    # 특정 article 조회하기.

    article = Article.objects.get(id=article_id)
    return render(request, 'board/article_detail.html', {
        'article': article,
    })
#  Update
def update_article(request, article_id):
    article = Article.objects.get(id=article_id)

    article.title = request.GET.get('title')
    article.content = request.GET.get('content')

    article.save()

    return redirect(f'/board/{article.id}')


def edit_article(request,article_id):
    article = Article.objects.get(id=article_id)

    return render(request, 'board/edit_article.html', {'article': article})



# Delete


def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/')
