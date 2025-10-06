from django.urls import path
from users import views
from hub import views

urlpatterns = [
    path('', views.home, name="home"),
]

app_name = 'hub'