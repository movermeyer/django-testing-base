from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from testbase.unit import UnitTestCase


class TestCreateUser(UnitTestCase):
    def setUp(self):
        self.name = self.randStr()
        self.password = self.randStr()
        self.email = '{}@{}.com'.format(self.randStr(), self.randStr()).lower()

        self.createUser(self.name, self.password, email=self.email)
        self.user = User.objects.get(username=self.name)

    def test_createsRegularUserInDatabase(self):
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_createsUserWithGivenEmail(self):
        self.assertEqual(self.email, self.user.email)

    def test_createsUserWithNonEmptyFirstName(self):
        self.assertNotEqual('', self.user.first_name)

    def test_createsUserWithNonEmptyLastName(self):
        self.assertNotEqual('', self.user.last_name)

    def test_createsUserWithGivenPassword(self):
        self.assertTrue(check_password(self.password, self.user.password))

