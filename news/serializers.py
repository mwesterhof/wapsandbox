from rest_framework import serializers

from .models import NewsArticle


class NewsArticleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return self.context['request'].parent_page.reverse(
                'article_detail', pk=obj.pk)

    class Meta:
        model = NewsArticle
        fields = '__all__'
