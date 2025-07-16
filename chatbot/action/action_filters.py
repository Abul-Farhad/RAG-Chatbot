from django_filters import rest_framework as filters
from chatbot.models import Product
from django.contrib.postgres.search import SearchVector, SearchQuery
class ProductFilter(filters.FilterSet):
    search_brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    search_model = filters.CharFilter(field_name='model', lookup_expr='icontains')
    search_review = filters.CharFilter(method='filter_review')

    def filter_review(self, queryset, name, value):
        return queryset.annotate(
            search=SearchVector('reviews', config='english')
        ).filter(search=SearchQuery(value, config='english'))

    class Meta:
        model = Product
        fields = ['search_brand', 'search_model', 'search_review', 'quantity']