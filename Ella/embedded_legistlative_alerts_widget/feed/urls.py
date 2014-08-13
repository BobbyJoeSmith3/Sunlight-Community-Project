from django.conf.urls import patterns, url

from feed import views

#URL for embedded legislative widgets feed
urlpatterns = patterns('',
	url(r'^$', views.feed_index, name='feed_index'),
)

#URL for widget generator user interface
urlpatterns = patterns('', 
	url(r'^$', views.widget_generator, name='widget_generator'),
)