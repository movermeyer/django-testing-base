# Base Test Case

**Canonical name**: `testbase.BaseTestCase`

`BaseTestCase` is an abstract class which provides testing tools that are common to both unit and browser tests. Both 
[UnitTestCase](unit/unit.md) and [BrowserTestCase](browser/browser.md) derive from `BaseTestCase`.

## Properties

### loggedInUser

The `User` object that was logged into the site using `logInAs`.

## Methods

### randStr(length=10)

Create a random string of the given length. The string will consist of only ASCII letters and digits.

### createUser(userName=None, password=None, *, email=None)
### createAdminUser(userName=None, password=None, *, email=None)
### createSuperUser(userName=None, password=None, *, email=None)

Create a new user in the database. Any arguments not given will be generated randomly. The `createAdminUser` gets the
`is_staff` flag while `CreateSuperUser` gets both the `is_staff` and `is_superuser` flags. Users are also given
randomly generated first and last names.

### logInAs(user=None, *, password=None) -> User

Log the specified user into the site. If no user is given then one will be created.

The `password` keyword argument only needs to be supplied if the user was _not_
created using one of the `createUser` methods or if the code needs to give a purposefully incorrect 
password.

This method returns the logged in user upon success.

For unit tests this method will log in using the Django test client (i.e. `self.client`).

For browser tests this method will direct the browser to the site's login page and log in using the form found there.
See [Browser Test Case](browser/browser.md) for details about how to describe the login page for the site.

### logOut()

Cause the currently logged in user to log out.

For unit tests this method will log out using the Django test client (i.e. `self.client`).

For browser tests this method will direct the browser trigger a log out operation. See 
[Browser Test Case](browser/browser.md) for details about how to describe the log out process for the site.

### expireSession(session)

Cause the given session object to expire immediately. When using `UnitTestCase` the `session` argument can be
omitted. In this case the test client's session (i.e. `self.client.session`) will be expired.

### assertEmailSent(numberOfEmails=1)

Asserts that the given number of emails was sent using Django's mail module.

### getEmailsWithSubject(subject)

Returns, as a list, all emails that were sent with the given subject.
