from django.core.urlresolvers import reverse
from testbase.unit import UnitTestCase
from testbase.unit.views import RequiresLogin


class TestRequiresLogin(UnitTestCase, RequiresLogin):
    def get_url(self):
      return reverse('requires_login')