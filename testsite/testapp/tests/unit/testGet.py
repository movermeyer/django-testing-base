from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase


class TestGet(UnitTestCase):
    def setUp(self):
        self.expected = self.randStr()

    def get_url(self):
        return reverse('withUrlFields', kwargs={'value': self.expected})

    def test_makesGetRequestToNamedUrlPattern(self):
        response = self.get('withUrlFields', value=self.expected)
        self.assertContains(response, self.expected)

    def test_makesGetRequestToUrlFromFactoryMethod(self):
        response = self.get()
        self.assertContains(response, self.expected)
