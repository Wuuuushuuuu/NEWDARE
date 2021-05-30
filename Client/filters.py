import django_filters

from .models import*

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = client
        fields = {'name', 'contact_no', 'email'}
