from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=127, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey("blog.Author")


class Post(models.Model):
    blog = models.ForeignKey("blog.Blog")
    posted_at = models.DateField(default=now)
    title = models.CharField(max_length=127, db_index=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    tags = models.ManyToManyField("blog.Tag")


class Comment(models.Model):
    commenter = models.ForeignKey("blog.Author")
    date = models.DateTimeField(default=now)
    post = models.ForeignKey("blog.Post")
    body = models.TextField()


class Tag(models.Model):
    tag = models.CharField(blank=True, null=True, max_length=127)
