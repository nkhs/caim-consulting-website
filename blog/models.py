from django.db import models


class BlogPost(models.Model):
    published_datetime = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30)
    content = models.TextField()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
