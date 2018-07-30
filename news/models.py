from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail_app_pages.models import AppPageMixin
from wagtailtrans.models import TranslatablePage

from products.models import Product


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    highlighted_product = models.ForeignKey(
        Product, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class NewsPage(AppPageMixin, TranslatablePage, Page):
    url_config = 'news.urls'
    product_page = ParentalKey(
        'products.ProductPage', null=True, on_delete=models.SET_NULL)

    settings_panels = TranslatablePage.settings_panels + [
        FieldPanel('product_page')
    ]
