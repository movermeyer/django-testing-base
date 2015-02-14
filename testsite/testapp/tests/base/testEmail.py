from django.core.mail import send_mail
from testbase.unit import UnitTestCase


class TestEmail(UnitTestCase):
    def setUp(self):
        self.subject = self.randStr()
        self.body = self.randStr()
        self.fromAddress = self.randStr()
        self.toAddress1 = self.randStr()
        self.toAddress2 = self.randStr()
        send_mail(self.subject, self.body, self.fromAddress, [self.toAddress1, self.toAddress2])
        send_mail(self.randStr(), self.randStr(), self.randStr(), [self.toAddress1])

    def test_assertEmailsSent(self):
        self.assertEmailSent(2)
        try:
            self.assertEmailSent(1)
            raise RuntimeError('No assertion with wrong number of emails')
        except AssertionError:
            pass



