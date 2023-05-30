from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    # breakpoint()
    # confirm_password = serializers.CharField()

    def create(self, validated_data):
        # customer_serializer = CustomerSerializer(validated_data.get('customer'))
        # customer_serializer.save()
        confirm_password = validated_data.pop('confirm_password')
        password = validated_data['password']

        username = validated_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("username already exists.")
        if password != confirm_password:
            raise serializers.ValidationError("password does not matched.")
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['first_name', 'last_name', 'email', 'phone_number', 'department',
        #           'is_staff', 'is_superuser', 'age', 'gender', 'profile_pic',
        #           'bio', 'password']
        fields = ['first_name', 'last_name', 'email', 'password',]
