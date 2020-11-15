from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        exclude = ("password", "groups", "is_staff", "is_active", "is_superuser", "last_login")


class UserCreationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"
    })
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password"
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        # if email and User.objects.filter(email=email).exist():
        #     raise serializers.ValidationError(
        #         {"email": "Email address must be unique"}
        #     )
        if password1 != password2:
            raise serializers.ValidationError({
                {"password": "The two passwords differ"}
            })
        user = User(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password1)
        user.save()
        return user
