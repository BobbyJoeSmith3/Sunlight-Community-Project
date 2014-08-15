# Import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from forms import WidgetGenerator
import feedparser
import requests

# Create your views here.


# Stand alone function that will parse the RSS feed xml data for Title, Description, and Publication Date.
def getScoutCollectionData(request):
	#Connect to widget generator form
	form = WidgetGenerator()
	#Validate that the info the user entered into the form is valid
	if request.method == 'POST':
		form = WidgetGenerator(request.POST)
		if form.is_valid():
			rss_url = form.cleaned_data['rss_url']
			# Parse the rss_url
			d = feedparser.parse(rss_url)
			# Create an empty list to put the dictionaries in
			posts = []
			# Fill up the empty list posts with dictionaries
			for entry in d.entries:
				# Create a dictionary for each post with title, pubdate, and content
				post = {}
				# Assign each key
				post['title'] = entry.title
				post['pub_date'] = entry.published
				post['description'] = entry.description
				posts.append(post)
			# Return the bucket
			return posts
	'''
	# Link to the RSS feed url *For now we'll use mine
	#rss_url = "feed:https://scout.sunlightfoundation.com/user/53cfcc6a0311036a060003be/native-america.rss"
	# Parse the rss_url
	d = feedparser.parse(rss_url)
	# Create an empty list to put the dictionaries in
	posts = []
	# Fill up the empty list posts with dictionaries
	for entry in d.entries:
		# Create a dictionary for each post with title, pubdate, and content
		post = {}
		# Assign each key
		post['title'] = entry.title
		post['pub_date'] = entry.published
		post['description'] = entry.description
		posts.append(post)
	# Return the bucket
	return posts
	'''
# Connect to the feed app template
def feed_index(request):
	# Create a variable collection_data for the getScoutCollectionData function below to getting the data to the html template
	collection_data = getScoutCollectionData(request)
	return render(request, 'feed/feed_index.html', {'collection_data': collection_data})

# Connect to widget generator template
def widget_generator(request):
	#Connect to the widget generator form
	form = WidgetGenerator()
	#Validate that the info the user entered into the form is valid
	if request.method == 'POST':
		form = WidgetGenerator(request.POST)
		if form.is_valid():
			rss_url = form.cleaned_data['rss_url']
			frame_height = form.cleaned_data['frame_height']
			frame_width = form.cleaned_data['frame_width']
			#Generate the HTML code to create the widget based on the the information the user entered
			widget_code = "<iframe src='" + "http://127.0.0.1:8000/feed/" + "' height='" + frame_height + "' width='" + frame_width + "'></iframe>"
	return render(request, 'feed/widget_gen.html', {'form': form})

