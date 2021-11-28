from django.core import serializers
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from .models import Article

from website.settings import BASE_DIR


class Home(ListView):
    model = Article
    template_name = 'article/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-views')[:3]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jumbotron'] = Article.objects.order_by(
            'c_time').last()  
        return context


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    template_name = 'article/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-c_time')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'

    # def get_queryset(self):
    #     return Article.objects.get(pk=self.kwargs['pk'])

def about_page(request):
    return render(request, 'article/about.html')


# FaV template
# def single_article_detail(request, article_id):
#     try:
#         article = Article.objects.get(pk=article_id)
#     except Article.DoesNotExist:
#         raise Http404("Article does not exist")
#     print(article.title, article.cover, "ddd")
#     return render(request, 'article/single_article.html', {'article': article})

from django.http import JsonResponse
from django.http import HttpResponse
from article.models import Article
from django.core import serializers
import json
def article_list(request):
    print(request.method)
    #articles = Article.objects.all()
    #serializer = serializers.serialize(articles, many=True)
    serializer = serializers.serialize("json", Article.objects.all())
    # js = Article.objects.all().values()
    # print(js)
    # js = json.loads(serializer)
    # print(js)
 
    # return JsonResponse(js, safe=False)
    return HttpResponse(serializer, content_type='application/json')



