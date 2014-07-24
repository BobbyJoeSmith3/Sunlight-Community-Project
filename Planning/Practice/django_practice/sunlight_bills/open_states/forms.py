from django import forms

class SearchBillForm(forms.Form):
	bill_number = forms.CharField(label="bill number", max_length=10)
	bill_name = forms.CharField(laberl="bill name", max_length=100)
	

class SearchApiKeyForm(forms.Form):
	api_key = forms.CharField(label="api key", max_length=50) 



#www.gmodules.com/ig/creator?url-http://feeds.labnl.org/labnol