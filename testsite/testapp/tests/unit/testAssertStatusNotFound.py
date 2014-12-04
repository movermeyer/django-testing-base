from testbase.unit import UnitTestCase


class TestAssertStatusNotFound(UnitTestCase):
    def test_raisesNoErrorIfStatusIsNotFound(self):
        response = self.get('http_status', status=404)
        self.assertResponseStatusIsNotFound(response)

    def test_raisesAssertionErrorIfStatusIsNotNotFound(self):
        response = self.get('http_status', status=200)
        self.assertRaises(AssertionError, self.assertResponseStatusIsNotFound, response)

    def test_checksLastResponseIfNoResponseGiven(self):
        self.get('http_status', status=404)
        self.assertResponseStatusIsNotFound()
