import django_filters
from django import forms
from .models import *
from django_filters import  CharFilter

class SearchFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='search')
   
    # tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(), 
    
    # widget = forms.CheckboxSelectMultiple
    
    # )

    class Meta:
        model = Todo
        fields = ['title']