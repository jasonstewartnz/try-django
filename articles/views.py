from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render

# @csrf_exempt - allows you to circumvent security (may be useful for REST API)
def article_create_view(request, id=None):
    context = {
    }

    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        print(f'Title is: {title}\n Content is: {content}')

        article_object = Article.objects.create(title=title,content=content)

        context['object'] = article_object
        context['created'] = True
        
    return render(request,'articles/create.html',context=context)

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

def article_search_view(request):

    print(request.GET)
    query_dict = request.GET 
    
    try:
        query = int(query_dict.get('q'))
    except: 
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        'object':article_obj
    }
    
    return render(request, 'articles/search.html', context=context)