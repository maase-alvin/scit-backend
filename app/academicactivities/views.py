"""
Views for the AcademicActivities APIs
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
    AcademicActivities,
)

from academicactivities import serializers


class AcademicActivitiesViewSet(viewsets.ModelViewSet):
    """View for manage AcademicActivities APIs."""
    serializer_class = serializers.AcademicActivitiesSerializer
    queryset = AcademicActivities.objects.all()
    
    
    def get_serializer_class(self):
        """Retrieve the list of AcademicActivities"""
        if self.action == 'retrieve' or self.action == 'update':
            return serializers.AcademicActivitiesDetailSerializer
        elif self.action == 'upload_image':
            return serializers.AcademicActivitiesImageSerializer
        
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new feedback"""
        serializer.save()
        
    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a AcademicActivities"""
        academicactivities = self.get_object()
        serializer = self.get_serializer(
            academicactivities, 
            data=request.data,
            partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
                )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )
    