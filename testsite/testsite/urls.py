from django.conf.urls import patterns, url
from testapp.views import requiresLogin, home, withUrlFields


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^withUrlFields/(?P<value>.*)/$', withUrlFields, name='withUrlFields'),
    url(r'^login_required/$', requiresLogin, name='requires_login'),
)

