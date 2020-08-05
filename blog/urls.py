from django.urls import path

from blog import views

urlpatterns = [
    path("bloghome/", views.blog_index, name="bloghome"),
    path("blog/<int:blog_id>/", views.blog_page, name="blogpage"),
    path("category/<int:catg_id>/", views.catg_page, name="catgpage"),
]
