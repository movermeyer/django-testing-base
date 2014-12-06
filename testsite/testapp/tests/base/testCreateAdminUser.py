from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from testbase.unit import UnitTestCase


class TestCreateAdminUser(UnitTestCase):
    def setUp(self):
        super().setUp()
        name = self.randStr()
        self.createAdminUser(userName=name)
        self.user = User.objects.get(username=name)

    def test_setsStaffFlag(self):
        self.assertTrue(self.user.is_staff)

    def test_doesNotSetSuperuserFlag(self):
        self.assertFalse(self.user.is_superuser)

