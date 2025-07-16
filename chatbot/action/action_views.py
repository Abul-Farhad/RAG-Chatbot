from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.Tools.tools import get_smartphone_data
from chatbot.action.action_filters import ProductFilter
from chatbot.action.action_serializers import ProductSerializer
from chatbot.models import Product

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        result = get_smartphone_data(search_brand="apple", search_model="14")
        # print(result)
        return Response(result, status=200)
