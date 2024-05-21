"""
Serializers for Academic Activities APIs
"""
from rest_framework import serializers

from core.models import (
    AcademicActivities
)
        
class AcademicActivitiesSerializer(serializers.ModelSerializer):
    """Serializer for Academic Activities"""
    
    class Meta:
        model = AcademicActivities
        fields = [
            'id',
            'name',
            'description',
            'duration',
            'amount',
            'related_information',
            'image',          
        ]
        read_only_fields = ['id']
        
        
class AcademicActivitiesDetailSerializer(AcademicActivitiesSerializer):
    """Serializer for Academic Activities Detail View."""
    class Meta(AcademicActivitiesSerializer.Meta):
        fields = AcademicActivitiesSerializer.Meta.fields

class AcademicActivitiesImageSerializer(serializers.ModelSerializer): 
    """Seriailizer for uploading images to academic Activities"""
    class Meta:
        model = AcademicActivities
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image':{'required': 'True'}}