# Unit Test Case

**Canonical name**: `testbase.unit.UnitTestCase`

The `UnitTestCase` class provides helper method for testing Django views. It derives from 
[django.test.TestCase](https://docs.djangoproject.com/en/dev/topics/testing/tools/#testcase) and 
[BaseTestCase](../base.md).

## Properties

### response

The HttpResponse object returned by the most recent call to the `get` method on this class.

## Methods

### get(self, urlPattern=None, *args, **kwargs)

This shortcut method replaces the following typical pattern:

    url = reverse('obj-detail', kwargs={'id': 123})
    response = self.client.get(url)

The _urlPattern_ argument, if given, provides a named url pattern to reverse and get using the standard test client. The
_args_ and _kwargs_ are passed to the equivalently named arguments of the Django 
[reverse](https://docs.djangoproject.com/en/dev/ref/urlresolvers/#reverse) function to derive the final URL. The above
example would thus become simply:

    self.get('obj-detail', id=123)

The response to the get request is both returned by this method and stored as the `response` property on the test
case.

If no _urlPattern_ is provided then this method will call `self.get_url()` to find the URL. This is particularly useful
when most or all tests in a suite operate on the same URL. For example:

    def get_url(self):
        return reverse('some_url', kwargs={'name': self.randStr()})
     
    def test_edge_case_number_54(self):
        self.get()
        ...

### assertResponseStatusIsOk(response=None)
### assertResponseStatusIsNotFound(response=None)

These methods check that the HTTP status of the given response object matches that named in the method. These methods
replace the following pattern:

    self.assertEqual(HttpResponseNotFound.status_code, response.status_code)

If no _response_ argument is given then these methods will test against `self.response`.

### assertContextValueEqual(self, response, contextVariableName, expectedValue)
### assertLastContextValueEqual(self, contextVariableName, expectedValue)

These methods check that the context of a response contains a value that matches the expected value. This replaces the
following pattern:

    self.assertEqual(expectedValue, response.context[contextVariableName])

The second form, where no response is given, tests against the context in `self.response`.

