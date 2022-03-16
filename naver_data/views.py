from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from naver_data.models import NaverData, NaverBlogData, NaverCafeData
from naver_data.serializer import NaverDataSerializer
from naver_data.util.pagenator import BlogListPaginationClass

'''
todo
1. respose 관련 작업.
2. 페이지넘김 처리.
'''


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


@permission_classes([AllowAny])
class NaverDataView(APIView):

    def get(self, request):
        paginator = StandardResultsSetPagination()
        serializer = NaverDataSerializer(data=request.query_params)
        serializer.is_valid()
        query = serializer.validated_data
        search_word = query.get('keyword')
        table = query.get('platform')
        model_dict = {'blog': NaverBlogData, 'cafe': NaverCafeData}
        results = model_dict[table].objects.filter(keyword=search_word).values()
        context = paginator.paginate_queryset(results, request)
        serializer = NaverDataSerializer(context, many=True) # serialize
        # return Response(status=200, data=results)
        # serializer = self.pagination_class(results)
        return Response(serializer.data, status=status.HTTP_200_OK)
