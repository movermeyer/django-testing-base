from django.conf.global_settings import LOGIN_URL
from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase


class TestLogout(UnitTestCase):
    def test_logsUserOut(self):
        loginRequiredUrl = reverse('requires_login')

        user = self.createUser()
        self.logInAs(user)
        self.client.get(loginRequiredUrl)

        self.logOut()
        response = self.client.get(loginRequiredUrl)

        expectedRedirect = '{}?next={}'.format(LOGIN_URL, loginRequiredUrl)
        self.assertRedirects(response, expectedRedirect)

