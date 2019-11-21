from rest_framework import serializers
from .models import Phone_number


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone_number
        fields = ['code', 'start_number', 'end_number', 'company', 'region']
