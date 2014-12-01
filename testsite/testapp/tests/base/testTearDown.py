from django.utils import translation
from testbase.unit import UnitTestCase


class TestTearDown(UnitTestCase):
    def setUp(self):
        translation.activate('de')

    def tearDown(self):
        super().tearDown()

        # language is reset to en
        self.assertEqual('en', translation.get_language())

    def test_tearDown(self):
        pass
