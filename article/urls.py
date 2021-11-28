from django.urls import path, include
from article import views
from article.models import Article

app_name = 'article'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<pk>', views.ArticleDetail.as_view(), name='detail'),
    path('about/', views.about_page, name='about-me'),
]
