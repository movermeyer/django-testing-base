from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase


class TestLogIn(UnitTestCase):
    def test_logsInUserWithCachedPassword(self):
        user = self.createUser()
        self.logInAs(user)
        response = self.get('requires_login')
        self.assertResponseStatusIsOk(response)

