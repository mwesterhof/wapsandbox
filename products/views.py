from django.views.generic import DetailView, ListView

from .models import Category, Product


class ProductViewMixin:
    def get_queryset(self, *args, **kwargs):
        is_promotional = self.parent_page.is_promotional

        categories = Category.objects.for_page(self.parent_page)
        qs = super().get_queryset(*args, **kwargs).filter(
            category__in=categories)

        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category[0])
        if is_promotional:
            qs = qs.filter(promoted=True)
        return qs


class ProductList(ProductViewMixin, ListView):
    model = Product


class ProductDetail(ProductViewMixin, DetailView):
    model = Product


class OrderProduct(ProductViewMixin, DetailView):
    model = Product
    template_name = 'products/order_product.html'
