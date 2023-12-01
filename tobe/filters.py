
# custom filter

from django_filters import rest_framework as filter
from .models import Tobe



class TobeFilter(filter.FilterSet):
    class Meta:
        model = Tobe
        fields = {
            'id' : ['range','lte','gte'],   # lte is less than or equal to , gte is greater than or equal to
            'name' : ['contains'],
            
        }
