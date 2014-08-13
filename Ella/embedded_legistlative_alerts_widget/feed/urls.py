from django.conf.urls import patterns, url

from feed import views

#URL for embedded legislative widgets feed
urlpatterns = patterns('',
	url(r'^$', views.feed_index, name='feed_index'),
	url(r'^widget_generator/$', views.widget_generator, name='widget_generator'),
)

