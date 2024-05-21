"""
Views for the Payment APIs
"""
from rest_framework import (
    viewsets,
    mixins,
    generics,
    status,
    )
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import (
    Payment,
)

from payment import serializers


class PaymentViewSet(viewsets.ModelViewSet):
    """View for manage Payment APIs."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PaymentDetailSerializer
    queryset = Payment.objects.all()
    
    def get_serializer_class(self):
        """Returns the serializer class for request."""
        if self.action == 'list':
            return serializers.PaymentSerializer
        
        return self.serializer_class
    
    def get_queryset(self):
        """Retrieve the list of payments"""
        queryset = self.queryset
        return queryset.order_by('-id').distinct()
    
    def perform_create(self, serializer):
        """Create a new payment"""
        serializer.save(user=self.request.user)
    