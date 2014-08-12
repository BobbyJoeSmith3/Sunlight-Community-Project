# Import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from forms import WidgetGenerator
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

# A function that will take user inputs to generate code for an iframe
#def generateiFrame():
	#rss_url = raw_input('Paste the rss URL for your SCOUT collection:')
	#frame_width = raw_input('What is your desired width in pixels for the iframe?:')
	#frame_height = raw_input('What is your desired height in pixels for the iframe?:')