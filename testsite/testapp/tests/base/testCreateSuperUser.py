from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from testbase.unit import UnitTestCase


class TestCreateAdminUser(UnitTestCase):
    def setUp(self):
        name = self.randStr()
        self.createSuperUser(userName=name)
        self.user = User.objects.get(username=name)

    def test_setsStaffFlag(self):
        self.assertTrue(self.user.is_staff)

    def test_setsSuperuserFlag(self):
        self.assertTrue(self.user.is_superuser)

