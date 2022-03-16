from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from naver_data.models import NaverBlogData


class NaverDataSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=30, default='all')
    platform = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    contents = serializers.CharField(max_length=900, required=False)
    writer = serializers.CharField(max_length=100, required=False)
    reg_date = serializers.DateTimeField(required=False)
    crawl_url = serializers.CharField(max_length=900, required=False)
    comment_cnt = serializers.IntegerField(required=False)
    like_cnt = serializers.IntegerField(required=False)

    class Meta:
        model = NaverBlogData
        fields = ['id', 'title', 'contents', 'keyword', 'platform', 'writer', 'reg_date', 'crawl_url', 'comment_cnt',
                  'like_cnt']

    def validate(self, attrs):
        keyword = attrs.get('keyword')
        if keyword is None:
            raise ValidationError('validation Error - Not found Keyword coulmns')
        return attrs
