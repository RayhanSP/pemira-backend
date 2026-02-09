from rest_framework import serializers


class LoginRequest(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    npm = serializers.CharField(min_length=10, max_length=10)
    major = serializers.CharField()

    def validate(self, attrs):
        if "@ui.ac.id" not in attrs["email"]:
            raise serializers.ValidationError("Email must be from UI")
        return attrs



class LoginResponse(serializers.Serializer):
    id = serializers.CharField ()
    email = serializers.EmailField()
    name = serializers.CharField()
    npm = serializers.CharField()
    major = serializers.CharField()
    batch = serializers.CharField()
    token = serializers.CharField()
