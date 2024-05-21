"""
URL mappings for the recipe app
"""
from django.urls import (
    path, 
    include,
)

from rest_framework.routers import DefaultRouter

from program import views

router = DefaultRouter()
router.register('programmes', views.ProgrammeViewSet)

app_name = 'programme'

urlpatterns = [
    path('', include(router.urls)),
]