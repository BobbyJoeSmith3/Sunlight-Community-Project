from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunlight_bills.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^open_states/', include('open_states.urls', app_name='open_states'))
   # url(r'^admin/', include(admin.site.urls)),
)
