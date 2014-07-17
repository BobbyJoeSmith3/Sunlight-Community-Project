import requests

#the init function is going to automatically generate properties onto that object. Self are things that don't change.

# class Sunlightclient(object):
# 	def __init__(self):
# 		self.apikey = "f353ff159606417785e8a8570aa38885"
# 		self.rooturl = "http://openstates.org/api/v1/bills/"

# # the request functon takes 3 arguments

# 	#def request(self, http_method="GET", **kwargs):
# 	#	params = {"apikey": "f353ff159606417785e8a8570aa38885"}
# 		response = requests.request(http_method, self.rooturl, params=params)
# 		return response

# We are calling the requests library that we imported
params = {"apikey": "f353ff159606417785e8a8570aa38885", "state": "tx"}
s = requests.get("http://openstates.org/api/v1/bills/", params=params)

json_response = s.text


