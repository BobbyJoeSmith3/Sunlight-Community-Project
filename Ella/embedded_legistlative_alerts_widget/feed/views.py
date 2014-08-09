# Import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import feedparser

# Create your views here.

# Connect to the feed app template
def index(request):
	# Create a variable collection_data for the getScoutCollectionData function below to getting the data to the html template
	collection_data = getScoutCollectionData()
	return render(request, 'feed/feed_index.html', {'collection_data': collection_data})

# Stand alone function that will parse the RSS feed xml data for Title, Description, and Publication Date.
def getScoutCollectionData():
	# Link to the RSS feed url *For now we'll use mine
	rss_url = "feed:https://scout.sunlightfoundation.com/user/53cfcc6a0311036a060003be/native-america.rss"
	# Parse the rss_url
	d = feedparser.parse(rss_url)
	# Display the title of the first post
	#return d.entries[0].title
	#Create an empty bucket
	titles = []
	# Fill up the bucket
	for entry in d.entries:
		titles.append(entry.title)
	# Return the bucket
	return titles
