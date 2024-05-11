"""
To render html web pages
"""

import random 
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request) 
    Return HTML as a response (We pick to return the response)
    """

    name = 'Justin'
    random_id = random.randint(1, 3)

    article_obj = Article.objects.get(id=random_id)

    context = {
        'title':article_obj.title,
        'id':article_obj.id,
        'content':article_obj.content
    }

    # could open file, read and format string
    # Django templates similar to this but take it to another level

    # another option, but rarely used
    # tmpl = get_template('home-view.html')
    # tmpl_string = tmpl.render(context=context)
    # HTML_STRING = tmpl_string

    HTML_STRING = render_to_string('home-view.html',context=context)

    return HttpResponse( HTML_STRING )