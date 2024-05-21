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
    Application,
)

from application import serializers


class ApplicationViewSet(viewsets.ModelViewSet):
    """View for manage Application APIs."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ApplicationDetailSerializer
    queryset = Application.objects.all()
    
    def get_serializer_class(self):
        """Returns the serializer class for request."""
        if self.action == 'list':
            return serializers.ApplicationSerializer
        
        return self.serializer_class
    
    def get_queryset(self):
        """Retrieve the list of applications"""
        queryset = self.queryset
        return queryset.order_by('-id').distinct()
    
    def perform_create(self, serializer):
        """Create a new applicaiton"""
        serializer.save(user=self.request.user)
    