from django.urls import include, path
from rest_framework import routers

from .views import ArticleDetail, ArticleList, NewsArticleViewSet


router = routers.DefaultRouter()
router.register(r'articles', NewsArticleViewSet, base_name='articles')


urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('api/', include(router.urls)),
]
