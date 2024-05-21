"""
Views for the School APIs
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
    School,
)

from school import serializers


class SchoolViewSet(viewsets.ModelViewSet):
    """View for manage School APIs."""
    serializer_class = serializers.SchoolDetailSerializer
    queryset = School.objects.all()
    
    def get_serializer_class(self):
        """Returns the serializer class for request."""
        if self.action == 'list':
            return serializers.SchoolSerializer
        
        return self.serializer_class
    
    def get_queryset(self):
        """Retrieve the list of feedback for the authenticated user"""
        queryset = self.queryset
        return queryset.order_by('-id').distinct()
    
    def perform_create(self, serializer):
        """Create a new feedback"""
        serializer.save()
    