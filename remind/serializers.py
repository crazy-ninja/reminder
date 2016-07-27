from rest_framework import serializers
from remind.models import RemindMe


class RemindMeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    email = serializers.CharField(required=False, max_length=150, allow_null=True)
    mobile = serializers.CharField(required=False, allow_null=True, max_length=10, min_length=10)
    date_time = serializers.DateTimeField(required=True, allow_null=True)
    message = serializers.CharField(required=True, max_length=1000)

    def create(self, validated_data):
        """
        Create and return a new `RemindMe` instance, given the validated data.
        """
        return RemindMe.objects.create(**validated_data)
