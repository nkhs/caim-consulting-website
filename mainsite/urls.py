from django.urls import path

from mainsite import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("contactform/", views.contactform),
    path("messageinput/", views.messageinput),
    path("query/<int:chat_id>/", views.queries, name="query"),
]
