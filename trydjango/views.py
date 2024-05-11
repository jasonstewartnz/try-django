"""
To render html web pages
"""

import random 
from django.http import HttpResponse

from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request) 
    Return HTML as a response (We pick to return the response)
    """

    name = 'Justin'
    random_id = random.randint(1, 3)

    context = {
        'title':article_obj.title,
        'id':article_obj.id,
        'content':article_obj.content
    }

    # could open file, read and format string
    # Django templates similar to this but take it to another level

    article_obj = Article.objects.get(id=random_id)

    HTML_STRING = f"""
    <h1>{article_obj.title} (id: {article_obj.id})</h1>
    <p>{article_obj.content}</p>
    """.format(article_obj=article_obj)

    return HttpResponse( HTML_STRING )