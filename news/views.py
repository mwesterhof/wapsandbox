from django.views.generic import DetailView, ListView

from .models import NewsArticle


class ArticleList(ListView):
    model = NewsArticle


class ArticleDetail(DetailView):
    model = NewsArticle
