from django import forms

from .models import Stock, StockItems


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'


class StockItemsForm(forms.ModelForm):

    class Meta:
        model = StockItems
        fields = '__all__'
