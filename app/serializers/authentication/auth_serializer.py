from rest_framework import serializers
from app.models.usermodel import User

class RegisterSerializer(serializers.ModelSerializer):
    user_created_for = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    employee_user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            "phone",
            "first_name",
            "last_name",
            "user_type",
            "employee_user",
            "user_created_for"
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
        def create(self,validated_data):
            password = "{0}_{1}".format(str(validated_data["phone"]),"123456") 
            user = User.objects.create(
                phone = validated_data["phone"],
                first_name = validated_data["first_name"],
                last_name = validated_data["last_name"],
                user_type = validated_data["user_type"],
                username = validated_data["first_name"],
            )
            user.set_password(password)
            return user


class AllUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"