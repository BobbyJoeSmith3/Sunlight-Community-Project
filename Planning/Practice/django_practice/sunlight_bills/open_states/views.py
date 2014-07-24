from django.http import HttpResponse
import requests

def index(request):
	return HttpResponse("Hello, world. Your bill is near!")

def staff_generator():
	pass

# This is the function that will pull the input field data: Api_key, bill_id, open_states_url

def api_styled_data(request):
	#api_key = "f353ff159606417785e8a8570aa38885"
	#bill_id = "HR1227"
	#open_states_url = "http://openstates.org/api/v1/bills/"
	params = {"apikey": "f353ff159606417785e8a8570aa38885", "bill_id": "B 19-0428"}
	s = requests.get("http://openstates.org/api/v1/bills/", params=params)
	json_response = s.text
	return HttpResponse(json_response)


def staff_results():
	pass
