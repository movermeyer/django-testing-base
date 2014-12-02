from django.conf.urls import patterns, url
from testapp.views import requiresLogin, home


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^login_required/$', requiresLogin, name='requires_login'),
)

