from accounts import views
from django.urls import path

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("accounts/sign_up/", views.sign_up, name="sign_up"),
]
