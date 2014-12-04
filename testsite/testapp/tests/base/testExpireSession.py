from django.conf.global_settings import LOGIN_URL
from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase


class TestExpireSession(UnitTestCase):
    def test_expiresUserSessionForNextRequest(self):
        loginRequiredUrl = reverse('requires_login')

        user = self.createUser()
        self.logInAs(user)
        self.client.get(loginRequiredUrl)

        self.expireSession(self.client.session)
        response = self.client.get(loginRequiredUrl)

        expectedRedirect = '{}?next={}'.format(LOGIN_URL, loginRequiredUrl)
        self.assertRedirects(response, expectedRedirect, target_status_code=404)

