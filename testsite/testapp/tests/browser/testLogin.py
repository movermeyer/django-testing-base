from django.core.urlresolvers import reverse
from testbase.browser import BrowserTestCase, PageObject
from testbase.browser import SimpleLoginPage


class LoginRequiredPage(PageObject):
    _urlPattern = 'requires_login'


class TestBrowserLogin(BrowserTestCase):
    _pageClass = LoginRequiredPage
    _loginPage = SimpleLoginPage

    def test_startsAtAuthenticatedPageUnderTest(self):
        expected = self.live_server_url + reverse('requires_login')
        self.assertEqual(expected, self.browser.current_url)

    def test_subsequentTestsDoNotRequireAnotherLogin(self):
        expected = self.live_server_url + reverse('requires_login')
        self.assertEqual(expected, self.browser.current_url)

