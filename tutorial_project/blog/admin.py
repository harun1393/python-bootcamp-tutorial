from django.contrib import admin

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth"]
    search_fields = ["first_name", "last_name", "bio"]

admin.site.register(Author, AuthorAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title"]

admin.site.register(Blog, BlogAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "blog", "posted_at"]
    list_filter = ["is_draft", "blog"]
    search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

admin.site.register(Tag, TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["commenter", "post"]

admin.site.register(Comment, CommentAdmin)
