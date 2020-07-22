from django.db import models

# Create your models here.
class Query(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=500)
    resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Queries"
