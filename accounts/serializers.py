from rest_framework import serializers
from .models import HrAccount

class HrAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = HrAccount
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        return HrAccount.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.password = validated_data['password']  # No hashing
        instance.save()
        return instance
