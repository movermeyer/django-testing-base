from django.core.urlresolvers import reverse
from django.test import TestCase
from testbase import BaseTestCase


class UnitTestCase(TestCase, BaseTestCase):
    def __init__(self, methodName):
        BaseTestCase.__init__(self)
        super().__init__(methodName)

    def tearDown(self):
        BaseTestCase.tearDown(self)
        super().tearDown()

    def logInAs(self, user, *, password=None):
        username = user.username
        password = self.getPasswordForUser(user, password)

        result = self.client.login(username=username, password=password)
        if not result:
            raise RuntimeError('Failed to login as user [{}] with password [{}]'.format(username, password))
        self._loggedInUser = user

    def logOut(self):
        self.client.logout()

    def get_url(self):
        raise RuntimeError('UnitTestCase.get() called with no urlPattern but no get_url() method provided')

    def get(self, urlPattern=None, *args, **kwargs):
        if urlPattern is None:
            url = self.get_url()
        else:
            url = reverse(urlPattern, args=args, kwargs=kwargs)
        return self.client.get(url)

    def expireSession(self, session=None):
        if session is None:
            session = self.client.session
        super().expireSession(session)

    def assertResponseStatusIsOk(self, response):
        self.assertEqual(200, response.status_code)

    def assertResponseStatusIsNotFound(self, response):
        self.assertEqual(404, response.status_code)

    def assertResponseStatusIsUnauthorized(self, response):
        self.assertEqual(401, response.status_code)

    def assertContextValueEqual(self, response, contextVariableName, expectedValue):
        if contextVariableName not in response.context:
            raise AssertionError('Variable {} not found in context'.format(contextVariableName))
        self.assertEqual(expectedValue, response.context[contextVariableName])

