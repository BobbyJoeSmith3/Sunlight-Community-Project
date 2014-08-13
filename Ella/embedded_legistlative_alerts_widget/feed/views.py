# Import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from forms import WidgetGenerator
import feedparser

# Create your views here.

# Connect to the feed app template
def feed_index(request):
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


# Connect to widget generator template
def widget_generator(request):
	form = WidgetGenerator()
	if request.method == 'POST':
		form = WidgetGenerator(request.POST)
	if form.is_valid():
		rss_url = form.cleaned_data['rss_url']
		frame_height = form.cleaned_data['frame_height']
		frame_width = form.cleaned_data['frame_width']
	return render(request, 'feed/widget_gen.html', {'form': form})

