from django.db import models


class BlogPost(models.Model):
    published_datetime = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to="blogimages/%Y/%m/%d/", null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.category}: {self.title}"

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
