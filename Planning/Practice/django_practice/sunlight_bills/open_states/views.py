from django.http import HttpResponse
from django.template import Context #this allows you to pass data from the Controller to the view to your template
from django.shortcuts import render 
import requests
from forms import SearchBillForm

def index(request):
	form = SearchBillForm
	c = Context({
		"form": form  #the key form is set to the data variable form 
		})
	return render(request, "open_states/index.html", c)

def get_api():
	if request.method == 'POST': # If the form has been submitted...# ContactForm was defined in the previous section
		form = SearchBillForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
         # Process the data in form.cleaned_data
         bill_number = form.cleaned_data['bill number']
         bill_name = form.cleaned_data['bill name']
         state = form.cleaned_data['state']
         return HttpResponseRedirect("/open_states/")
        else:
        	form = SearchBillForm() # An unbound form

        return render(request, 'api_call.html', {
        'form': form,
    })


# This is the function that will pull the input field data: Api_key, bill_id, open_states_url

def api_styled_data(request):
	#api_key = "f353ff159606417785e8a8570aa38885"
	#bill_id = "HR1227"
	#open_states_url = "http://openstates.org/api/v1/bills/"
	#params = {"apikey": "f353ff159606417785e8a8570aa38885", "bill_id": "B 19-0428"}
	params = {"apikey": "f353ff159606417785e8a8570aa38885", "form": form} #parameters from the openstates api
	s = requests.get("http://openstates.org/api/v1/bills/", params=params)
	json_response = s.json()
	#return HttpResponse(json_response)
	return render(request, "open_states/index.html", json_response)


def staff_results():
	pass
