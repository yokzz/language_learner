from django.urls import path
from users import views
from users.views import RegisterView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]

# router = DefaultRouter()
# router.register()
# urlpatterns = router.urls
