from django import forms

# These forms will take user inputs to formulate the html code the user will need in embed the widget on their webpage
class WidgetGenerator(forms.Form):
	rss_url = forms.URLField(label="url:")
	frame_height = forms.IntegerField(label="widget height:")
	frame_width = forms.IntegerField(label="widget width:")
