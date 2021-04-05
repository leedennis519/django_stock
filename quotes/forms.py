from django import forms
from .models import Stock

# we just want the ModelFrom from forms within django library
class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["ticker"]