from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from naver_data.models import NaverData
from naver_data.serializer import NaverDataSerializer

'''
todo
1. respose 관련 작업.
2. 페이지넘김 처리.
'''
class NaverDataView(APIView):
    def get(self, request):
        serializer = NaverDataSerializer(data=request.query_params)
        serializer.is_valid()
        query = serializer.validated_data
        search_word = query.get('keyword')
        res = NaverData.objects.filter(keyword=search_word).values()

        # pagination 구현할것.
        return Response(status=200, data=res)
