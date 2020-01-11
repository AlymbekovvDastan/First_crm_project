import django_filters
from django_filters import DateFilter, CharFilter
from accounts.models import *

class OrderFilter(django_filters.FilterSet):
	start_data = DateFilter(field_name='date_created', lookup_expr='gte')
	end_data = DateFilter(field_name='date_created', lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created',]