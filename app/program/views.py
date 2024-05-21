"""
Views for the Programme APIs
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
    Programme,
)

from program import serializers


class ProgrammeViewSet(viewsets.ModelViewSet):
    """View for manage Programmes APIs."""
    serializer_class = serializers.ProgrammeSerializer
    queryset = Programme.objects.all()
    
    
    def get_serializer_class(self):
        """Retrieve the list of programmes"""
        if self.action == 'retrieve' or self.action == 'update':
            return serializers.ProgrammeDetailSerializer
        elif self.action == 'upload_image':
            return serializers.ProgrammeImageSerializer
        
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new programme"""
        serializer.save()
        
    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a Programme"""
        programme = self.get_object()
        serializer = self.get_serializer(
            programme, 
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
    