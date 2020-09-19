from django.urls import path

from blog import views

urlpatterns = [
    path(
        "publication/<int:publication_id>/",
        views.publication_page,
        name="publicationpage",
    ),
    path("category/<int:catg_id>/", views.catg_page, name="catgpage"),
]
