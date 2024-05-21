"""
URLs mappings for the Payment App
"""
from django.urls import (
    path,
    include,
)

from payment import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('payments', views.PaymentViewSet)

app_name = 'payment'

urlpatterns = [
    path('', include(router.urls)),
]