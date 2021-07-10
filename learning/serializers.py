from rest_framework import serializers
from .models import Address, Student


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, required=False)
    
    class Meta:
        model = Student
        fields = '__all__'