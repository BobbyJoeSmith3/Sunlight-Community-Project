from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
#import requests

# Create your views here.
def index(request):
	return render(request, 'feed/feed_index.html')