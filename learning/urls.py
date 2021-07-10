from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .api import AddresViewSet, StudentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'address', AddresViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path ('api/auth', views.obtain_auth_token),
    path('api/', include(router.urls + [path('auth', views.obtain_auth_token)])),
]
