"""
Serializers for School APIs
"""
from rest_framework import serializers

from core.models import School


class SchoolSerializer(serializers.ModelSerializer):
    """Serializer for School"""
    
    class Meta:
        model = School
        fields = [
            'id',
            'name',
            'telephone',
            'email',
            'address',          
        ]
        read_only_fields = ['id']
        
        
class SchoolDetailSerializer(SchoolSerializer):
    """Serializer for School Detail View."""
    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields