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

def staff_generator():
	pass

# This is the function that will pull the input field data: Api_key, bill_id, open_states_url

def api_styled_data(request):
	#api_key = "f353ff159606417785e8a8570aa38885"
	#bill_id = "HR1227"
	#open_states_url = "http://openstates.org/api/v1/bills/"
	#params = {"apikey": "f353ff159606417785e8a8570aa38885", "bill_id": "B 19-0428"}
	params = {"apikey": "f353ff159606417785e8a8570aa38885", "form": form}
	s = requests.get("http://openstates.org/api/v1/bills/", params=params)
	json_response = s.text
	#return HttpResponse(json_response)
	return render(request, "open_states/index.html", json_response)


def staff_results():
	pass
