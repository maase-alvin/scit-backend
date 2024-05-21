"""
URLs mappings for the Application App
"""
from django.urls import (
    path,
    include,
)

from application import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('applicaitons', views.ApplicationViewSet)

app_name = 'application'

urlpatterns = [
    path('', include(router.urls)),
]