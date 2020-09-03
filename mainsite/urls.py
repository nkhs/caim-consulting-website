from django.urls import path

from mainsite import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("contactform/", views.contactform),
    path("messageinput/", views.messageinput),
    path("subscribe/", views.subscription),
    path("chat/<int:chat_id>/", views.chats, name="chat"),
    path("board/<slug:member>/", views.advisory_board, name="advisory_board"),
]
