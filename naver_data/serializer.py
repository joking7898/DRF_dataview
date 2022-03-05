from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class NaverDataSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=30, default='all')

    def validate(self, attrs):
        keyword = attrs.get('keyword')
        if keyword is None:
            raise ValidationError('validation Error - Not found Keyword coulmns')
        return attrs

