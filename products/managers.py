from django.db import models


class CategoryManager(models.Manager):
    def for_page(self, page):
        qs = super().get_queryset()
        if page.categories.exists():
            return qs.filter(pages__product_page=page)
        return qs
