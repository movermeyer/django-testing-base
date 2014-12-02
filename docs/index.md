# Django Testing Base

[![Latest Version](https://pypip.in/version/django-testing-base/badge.svg?text=version)](https://pypi.python.org/pypi/django-testing-base/)
[![Development Status](https://pypip.in/status/django-testing-base/badge.svg)](https://pypi.python.org/pypi/django-testing-base/)
[![Downloads](https://pypip.in/download/django-testing-base/badge.svg?period=month)](https://pypi.python.org/pypi/django-testing-base/)
[![Supported Python versions](https://pypip.in/py_versions/django-testing-base/badge.svg)](https://pypi.python.org/pypi/django-testing-base/)
[![License](https://pypip.in/license/django-testing-base/badge.svg)](https://pypi.python.org/pypi/django-testing-base/)

Django Testing Base provides base Test Case and mixin classes that encapsulate common testing operations and patterns. 
They do  the "right" thing whether you're testing individual units of code or entire live pages using selenium.

## Features

- Generate test data
- Create and login users
- Common assertions
- Run selenium tests at different browser dimensions
- Base implementation of Page Object pattern

An example unit test:

    from testbase.unit import UnitTestCase
    
    class TestMyView(UnitTestCase):
        def test_somethingWithAUser(self):
            user = self.createUser()
            response = self.client.get(reverse('the_url'))
            self.assertResponseStatusIsOk(response)
            self.assertEqual(user.username, response.context['the_guy'])

An example browser test using the Page Object pattern:

    from testbase.browser import PageObject, BrowserTestCase
    
    class MyPage(PageObject):
        _urlPattern = 'named_url_pattern'
        _pageName = 'My Super Page'
        
        def click_link(self):
            link = self.browser.find_element_by_id('link_to_another_page')
            link.click()
    
    class TestMyPage(BrowserTestCase):
        _pageClass = MyPage
        _requiresLogin = True
        
        def __init__(self, methodName):
            super().__init__(methodName)
            self.thing = Thing.objects.create()
            self._urlFields['objectId'] = thing.pk
        
        def test_linkGoesToOtherPage(self):
            self.page.click_link()
            OtherPage(self.browser, otherPageField = 'some value')
    
## Installation

Install Django Testing Base using pip:

    pip install django-testing-base

## Contribute

- Issue Tracker: [https://github.com/tctimmeh/django-testing-base/issues](https://github.com/tctimmeh/django-testing-base/issues)
- Source Code: [https://github.com/tctimmeh/django-testing-base](https://github.com/tctimmeh/django-testing-base)

## License

The project is licensed under the MIT license.