from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }

    return render(request,'articles/detail.html',context=context)