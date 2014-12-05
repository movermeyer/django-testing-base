# Browser Test Case

**Canonical Name**: `testbase.browser.BrowserTestCase`

The `BrowserTestCase` works together with a `PageObject` to help test a single page of the site. Create a new Browser 
Test Case like this:

    class TestGreatPage(BrowserTestCase):
        _pageClass = GreatPageObject
        
        def setUp(self):
            self._urlFields['url_argument'] = 'someValue'
            super().setUp()

In this example the class-level `_pageClass` attribute is defined to describe the page under test. This attribute
names the `PageObject` class which describes the page. In this example the page object is describing a URL which 
requires parameters. The values for these parameters are specified in the `_urlFields` property during the `setUp()`
method. Note that the superclass setUp is called **after** setting up the URL fields. This is because it is 
`BrowserTestCase.setUp()` which directs the browser to the page under test.

## Class Properties

The `BaseTestCase` class uses a few class-level attributes to control it's behaviour.

### _pageClass

The class of the [PageObject](./pageobject.md) representing a page under test.

### _windowWidth
### _windowHeight

The dimensions of the browser window. Use this to test responsive designs at different browser sizes.

### _loginPage

The class of the [PageObject](./pageobject.md) for the site's login page. If this is given then the test
suite will use this page to log in a randomly created user before any tests are run. 

A simple login page, [SimpleLoginPage](https://github.com/tctimmeh/django-testing-base/blob/master/testbase/browser/simpleLoginPage.py), 
is provided which demonstrates the interface that must be implemented. Derive from `SimpleLoginPage` 
to add more functionality or override the default implementation. If the interface prescribed by 
`SimpleLoginPage` is not suitable for the project then override `BrowserTestCase.logInAs` to perform as desired.

## Properties

### _urlFields

A dictionary of variable parameters to use when browsing to the page described by `_pageClass`. These will be
passed to the django `reverse` function as _kwargs_.

### browser

The selenium webdriver object for this page. Use this when creating a new page object.

## Methods

### browseToPage(cls, **urlFields)

Direct the browser to the page described by [PageObject](./pageobject.md) class, _cls_, and return a new instance
of the page object. URL parameters required for the page object are provided as keyword arguments.

### browseToPageUnderTest()

Reset the browser to the page under test as specified by `_pageClass` and `_urlFields`.

### logInAs(user, * password=None)

Logs in the specified user by browsing to the login page described by `_loginPage`. This method enters the user's
name and password by calling `enter_username(username)` and `enter_password(password)` on the login page object 
then submits the login by calling `submit_login()`.

This method is called automatically during `suiteSetUp()` if a `_loginPage` is provided. It does not normally
need to be called manually.

### logOut()

There is no default implementation of `logOut()`. Override this method on a derived test case to enable logout
functionality if needed.

