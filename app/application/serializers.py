"""
Serializers for Application APIs
"""
from rest_framework import serializers

from core.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    """Serializer for Application"""
    
    class Meta:
        model = Application
        fields = [
            'id',
            'programme',
            'academic_activities',
            'payment',
            'status',
            'created_at',          
        ]
        read_only_fields = ['id',
                            'created_at']
        
        
class ApplicationDetailSerializer(ApplicationSerializer):
    """Serializer for Application Detail View."""
    class Meta(ApplicationSerializer.Meta):
        fields = ApplicationSerializer.Meta.fields