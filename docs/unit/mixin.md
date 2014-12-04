# Unit Testing Mixins

The following mixin classes add common tests to an existing test suite.

## RequiresLogin

Checks that a view is only accessible by an authenticated user. The test case class must implement the `get_url` method
(as described in [Unit Test Case](./unit.md)) to provide the tests with the URL under test. 

This mixin class provides the following tests:

* a get request for a non-authenticated user redirects to the login page
* a get request for an authenticated user returns an Ok HTTP status

