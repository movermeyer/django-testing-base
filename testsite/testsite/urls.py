from django.conf.urls import patterns, url
from testapp.views import requiresLogin, home, withUrlFields, httpStatus


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^withUrlFields/(?P<value>.*)/$', withUrlFields, name='withUrlFields'),
    url(r'^login_required/$', requiresLogin, name='requires_login'),
    url(r'^http_status/(?P<status>\d+)/$', httpStatus, name='http_status'),
    url(r'^accounts/login/$', home, name='account_login'),
)

