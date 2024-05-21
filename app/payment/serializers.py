"""
Serializers for Payment APIs
"""
from rest_framework import serializers

from core.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment"""
    
    class Meta:
        model = Payment
        fields = [
            'id',
            'programme',
            'academic_activities',
            'amount',
            'method',
            'status',
            'created_at',          
        ]
        read_only_fields = ['id',
                            'created_at']
        
        
class PaymentDetailSerializer(PaymentSerializer):
    """Serializer for Payment Detail View."""
    class Meta(PaymentSerializer.Meta):
        fields = PaymentSerializer.Meta.fields