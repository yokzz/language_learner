from django.urls import path
from users import views

urlpatterns = [
    path("sign-up/", views.signup_view, name="sign-up"),
    path("sign-in/", views.signin_view, name="sign-in"),
]
