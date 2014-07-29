from django import forms

#  For choice field type for sunlight apis and states, set variables to populate input fields

SUNLIGHT_APIS = (
        ('1', 'Congress'),
        ('2', 'States'),
)

#django-localflavor install with pip in my virtualenvironment
STATES = (
        ('1', 'Alaska'),
        ('2', 'Alabama'),
        ('3', 'Arkansas'),
        ('4', 'American Samoa'),
        ('5', 'Arizona'),      
)

# This form will have 3 field ojects: bill_number, bill_name, and state. bill_number and bill_name will have a character field type and states will have a choice field type.
 
class SearchBillForm(forms.Form):
	api_call = forms.ChoiceField(label="open congress or open states", choices=SUNLIGHT_APIS)
	bill_number = forms.CharField(label="bill number", max_length=10)
	bill_name = forms.CharField(label="bill name", max_length=100, required=False)
	state = forms.CharField(label="state", max_length=5)

#class SearchApiKeyForm(forms.Form):
#api_key = forms.CharField(label="api key", max_length=50) 
#www.gmodules.com/ig/creator?url-http://feeds.labnl.org/labnol