from blog.models import Category, Publication
from django.contrib import admin


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "published_datetime",
        "last_modified_datetime",
        "category",
        "title",
    )
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    search_fields = ("name",)
