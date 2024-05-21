"""
URL mappings for the recipe app
"""
from django.urls import (
    path, 
    include,
)

from rest_framework.routers import DefaultRouter

from academicactivities import views

router = DefaultRouter()
router.register('academicactivities', views.AcademicActivitiesViewSet)

app_name = 'academicactivities'

urlpatterns = [
    path('', include(router.urls)),
]