from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
# Create your views here.


def article_view(request, id):

    article_obj = Article.objects.get(id=id)

    context = {
        'title':article_obj.title,
        'id':article_obj.id,
        'content':article_obj.content
    }


    HTML_STRING = render_to_string('article-view.html',context=context)

    return HttpResponse( HTML_STRING )