from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import NewsArticle


@modeladmin_register
class NewsArticleAdmin(ModelAdmin):
    model = NewsArticle
    menu_label = 'News articles'
