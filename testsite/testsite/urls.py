from django.conf.urls import patterns, url
from testapp.views import requiresLogin


urlpatterns = patterns('',
    url(r'^login_required/$', requiresLogin, name='requires_login'),
)

