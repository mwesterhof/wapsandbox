from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import NewsArticle
from .serializers import NewsArticleSerializer


class ArticleList(ListView):
    model = NewsArticle


class ArticleDetail(DetailView):
    model = NewsArticle


class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    authentication_classes = []

    serializer_class = NewsArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title',)

    def get_queryset(self, *args, **kwargs):
        return NewsArticle.objects.all()

    @action(methods=['patch'], detail=True)
    def like_article(self, request, pk):
        self.get_queryset().filter(pk=pk).update(
                like_count=F('like_count') + 1)
        return Response()

    @action(methods=['patch'], detail=True)
    def dislike_article(self, request, pk):
        self.get_queryset().filter(pk=pk, like_count__gte=1).update(
                like_count=F('like_count') - 1)
        return Response()
