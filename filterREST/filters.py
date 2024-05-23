from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    # lookup_expr='icontains' : 대소문자를 구분하지 않고, 해당 필드가 지정된 문자열을 포함하고 있는지 검사
    # 해당 필터를 통해 name 필드에서 부분 일치 검색을 수행
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    # lte : less than or equal to
    # lookup_expr='lte' : 해당 필드가 지정된 값 이하인지 검사
    # 해당 필터를 통해 price가 쿼리 매개변수로 전달된 값보다 작거나 같은 모든 제품을 반환
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    # gte : greater than or equal to
    # lookup_expr='gte' : 해당 필드가 지정된 값 이상인지 검사
    # 해당 필터를 통해 price가 쿼리 매개변수로 전달된 값보다 크거나 같은 모든 제품을 반환
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')

    # 이 필터는 in_stock 필드의 값이 True 또는 False인 제품을 필터링 하는데 사용
    # 쿼리에서 in_stock=True를 지정하면 재고가 있는 제품만 반환
    in_stock = filters.BooleanFilter()


    class Meta:
        model = Product
        fields = ['name', 'price', 'in_stock']