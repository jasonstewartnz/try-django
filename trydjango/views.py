"""
To render html web pages
"""

import random 
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request) 
    Return HTML as a response (We pick to return the response)
    """

    name = 'Justin'
    random_id = random.randint(1, 3)

    article_queryset = Article.objects.all() 

    context = {
        'object_list': article_queryset
    }


    HTML_STRING = render_to_string('home-view.html',context=context)

    return HttpResponse( HTML_STRING )