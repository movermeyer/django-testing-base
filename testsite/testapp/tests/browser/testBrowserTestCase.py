from django.core.urlresolvers import reverse
from testbase.browser import BrowserTestCase
from testbase.browser import PageObject


class HomePage(PageObject):
    _urlPattern = 'home'

class FieldsPage(PageObject):
    _urlPattern = 'withUrlFields'

class TestBrowserTestCase(BrowserTestCase):
    _pageClass = FieldsPage
    _windowWidth = 500
    _windowHeight = 400

    def setUp(self):
        self.value = self.randStr()
        self._urlFields['value'] = self.value
        super().setUp()

    def test_opensBrowserToCorrectPage(self):
        expectedUrl = self.live_server_url + reverse('withUrlFields', kwargs={'value': self.value})
        self.assertEqual(expectedUrl, self.browser.current_url)

    def test_browsingToNewPageFetchesPageForPageObject(self):
        self.browseToPage(HomePage)
        expectedUrl = self.live_server_url + reverse('home')
        self.assertEqual(expectedUrl, self.browser.current_url)

    def test_browsingToPageUnderTestRetunsToTestCasePage(self):
        self.browseToPage(HomePage)
        self.browseToPageUnderTest()

        expectedUrl = self.live_server_url + reverse('withUrlFields', kwargs={'value': self.value})
        self.assertEqual(expectedUrl, self.browser.current_url)

    def test_browserDimensionsMatchThoseGivenOnTestCase(self):
        size = self.browser.get_window_size()
        self.assertEqual(self._windowWidth, size['width'])
        self.assertEqual(self._windowHeight, size['height'])

