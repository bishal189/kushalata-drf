from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user




class MembershipUpdateSerializer(serializers.Serializer):
    membership_type = serializers.ChoiceField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')])

    def update(self, instance, validated_data):
        instance.set_membership(validated_data['membership_type'])
        return instance        