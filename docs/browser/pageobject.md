# Page Object

**Canonical Name**: `testbase.browser.PageObject`

A `PageObject` represents a single page within a web site. It's purpose is to abstract the structure of the page and 
provide methods to query and interact with the page as it is loaded in the browser. Tests should almost never interact
with selenium directly. Instead, create methods on a page object to handle those interactions.

Create page object by deriving from the base PageObject and providing some information about your page:

    class GreatPage(PageObject):
        _urlPattern = 'some_named_url_pattern'
        _pageName = 'Page Name'
    
The page object makes use of two class-level attributes: `_urlPattern` and `_pageName`. The URL pattern specifies a 
named pattern from the site's URL config. The page name is a human readable description of the page. The page name is
optional but recommended as it is used in messages and error descriptions.

The simplest way to create a new instance of a page object is to browse to the page using the 
[BrowserTestCase](./browser.md).`browseToPage` method. A page object can also be instantiated directly by passing the 
selenium webdriver instance and any URL fields necessary for the URL pattern. For example:

    def test_somethingGreat(self):
        # this will browse to the page then create a new GreatPage object
        page = self.browseToPage(GreatPage, urlArgument=value)
        
        # this creates an instance of GreatPage without affecting the browser
        page = GreatPage(self.browser, urlArgument=value)

In either case, when a new PageObject is instantiated it immediately verifies that the browser's location matches the
URL that the object expects. If there is a mismatch of any kind then an error is raised.

## Properties

### browser

The selenium webdriver object for this page. Use this to query and interact with the page.
