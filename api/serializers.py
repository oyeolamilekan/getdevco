from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        lookup_field = 'slug'
        fields = ('id','user','topic','body')