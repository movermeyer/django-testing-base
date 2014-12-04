from testbase.unit import UnitTestCase


class TestAssertStatusOk(UnitTestCase):
    def test_raisesNoErrorIfStatusIsOk(self):
        response = self.get('home')
        self.assertResponseStatusIsOk(response)

    def test_raisesAssertionErrorIfStatusIsNotOk(self):
        response = self.get('http_status', status=500)
        self.assertRaises(AssertionError, self.assertResponseStatusIsOk, response)

    def test_checksLastResponseIfNoResponseGiven(self):
        self.get('home')
        self.assertResponseStatusIsOk()
