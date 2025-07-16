from rest_framework import serializers
from chatbot.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ['brand', 'model', 'price', 'quantity', 'reviews']