import datetime

from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_by = models.ForeignKey("auth.User", blank=True, null=True, related_name="+")
    updated_by = models.ForeignKey("auth.User", blank=True, null=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class BlogActivity(BaseModel):
    activity = models.CharField(max_length=127)
    user = models.ForeignKey("auth.User", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "[{}] {} Activity".format(self.timestamp, self.user)


class Author(BaseModel):
    first_name = models.CharField(help_text="THIS IS REPRESENTATION FOR FIRST NAME", max_length=127, blank=True, null=True)
    last_name = models.CharField(max_length=127, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        BlogActivity.objects.create(activity="An author just got saved",
                                    user=self.created_by)
        return super(Author, self).save(*args, **kwargs)

    def age(self):
        if self.date_of_birth:
            return int((datetime.date.today() - self.date_of_birth).days/365.)
        else:
            return -1

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __unicode__(self):
        return self.get_full_name()

class Blog(BaseModel):
    title = models.CharField(max_length=127, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey("blog.Author")

    def __unicode__(self):
        return self.title


class Post(BaseModel):
    blog = models.ForeignKey("blog.Blog")
    posted_at = models.DateField(default=now)
    title = models.CharField(max_length=127, db_index=True)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    tags = models.ManyToManyField("blog.Tag")

    def __unicode__(self):
        return self.title


class Comment(BaseModel):
    commenter = models.ForeignKey("blog.Author")
    date = models.DateTimeField(default=now)
    post = models.ForeignKey("blog.Post")
    body = models.TextField()

    def __unicode__(self):
        return self.commenter


class Tag(BaseModel):
    tag = models.CharField(blank=True, null=True, max_length=127)

    def __unicode__(self):
        return self.tag
