from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HrAccountViewSet

router = DefaultRouter()
router.register(r'hr-accounts', HrAccountViewSet, basename='hraccount')

urlpatterns = [
    path('', include(router.urls)),
]