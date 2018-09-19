from rest_framework import viewsets, pagination, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ArticleSerializer
from articles.models import Article
@api_view(['GET'])
def all_art(request,slug):
    slug = User.objects.get(username=slug)
    post = Article.objects.filter(user=slug)
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(post,request=request)
    serializer = ArticleSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)