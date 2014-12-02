from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase


class TestAssertContextValueEqual(UnitTestCase):
    def test_raisesNoErrorIfContextContainsExpectedValue(self):
        response = self.client.get(reverse('home'))
        self.assertContextValueEqual(response, 'context_var', 'expected')

    def test_raisesAssertionErrorIfValueIsIncorrect(self):
        response = self.client.get(reverse('home'))
        self.assertRaises(AssertionError, self.assertContextValueEqual, response, 'context_var', self.randStr())

    def test_raisesAssertionErrorIfContextValueNotPresent(self):
        response = self.client.get(reverse('home'))
        self.assertRaises(AssertionError, self.assertContextValueEqual, response, self.randStr(), self.randStr())
