import django_filters

from .models import Shop, Item


class ShopFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    owner = django_filters.CharFilter(field_name="owner__username", lookup_expr="icontains")
    
    class Meta:
        model = Shop
        fields = ['name', 'owner']
        
        
class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr="lt")
    shop = django_filters.CharFilter(field_name='shop__name', lookup_expr='icontains')
    
    class Meta:
        model = Item
        fields = ['name', 'price', 'price__gt', 'price__lt', 'shop']
    