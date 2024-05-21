"""
Serializers for Programme APIs
"""
from rest_framework import serializers

from core.models import (
    Programme
)
        
class ProgrammeSerializer(serializers.ModelSerializer):
    """Serializer for Programme"""
    
    class Meta:
        model = Programme
        fields = [
            'id',
            'name',
            'duration',
            'cost',
            'description',
            'image',          
        ]
        read_only_fields = ['id']
        
        
class ProgrammeDetailSerializer(ProgrammeSerializer):
    """Serializer for Programme Detail View."""
    class Meta(ProgrammeSerializer.Meta):
        fields = ProgrammeSerializer.Meta.fields

class ProgrammeImageSerializer(serializers.ModelSerializer): 
    """Seriailizer for uploading images to programme"""
    class Meta:
        model = Programme
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image':{'required': 'True'}}