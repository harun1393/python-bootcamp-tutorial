from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import filters

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth", "age", "bio"]

class AuthorWithoutBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "age"]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author Help Model
    """
    #serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ["first_name", "last_name", "bio"]
    ordering_fields = ["first_name", "last_name", "date_of_birth"]

    def get_serializer_class(self):
        if not self.request.user.is_anonymous():
            return AuthorSerializer
        else:
            return AuthorWithoutBioSerializer


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title", "description"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ["title", "content"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ["body"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["tag"]

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ["tag"]
