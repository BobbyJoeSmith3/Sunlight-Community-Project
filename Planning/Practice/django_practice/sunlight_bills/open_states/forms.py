from django import forms

class SearchStatesForm(forms.Form):
	state = forms.CharField(label="State", max_length=5)

