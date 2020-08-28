from django.urls import path

from accounts import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("accounts/sign_up/", views.sign_up, name="sign_up"),
]
