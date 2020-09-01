from django.conf import settings
from django.db import models

from tinymce.models import HTMLField


class BlogPost(models.Model):
    published_datetime = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to="blogimages/%Y/%m/%d/", null=True, blank=True)
    gdrive = models.URLField(blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    author_name = models.CharField(max_length=50, null=True, blank=True)
    draft = models.BooleanField(default=False)
    content = HTMLField()

    def __str__(self):
        return f"{self.category}: {self.title}"

    def save(self, *args, **kwargs):
        if not self.author_name:
            self.author_name = self.uploaded_by.get_full_name()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_datetime"]


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
