"""
URLs mappings for the School App
"""
from django.urls import (
    path,
    include,
)

from school import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('school', views.SchoolViewSet)

app_name = 'school'

urlpatterns = [
    path('', include(router.urls)),
]