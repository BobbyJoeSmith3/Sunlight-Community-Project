from django.conf.urls import patterns, url

from open_states import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
      url(r'^api_open/$', views.api_styled_data, name='api data')
)