from rest_framework import serializers
from account.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True},
                        'username': {"required": False}}

    def create(self, validated_data):
        # password = validated_data.get('password')
        user = MyUser(**validated_data)
        user.set_password(user.password)
        user.is_active = False
        user.save()
        return user
