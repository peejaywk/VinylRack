## Testing

### Table of Contents

[Test Strategy](#teststrategy)

[User Story Testing](#userstorytesting)

[Functional/Features Testing](#functionaltesting)

[Code Validation](#codevalidation)

[Bugs / Issues](#bugsissues)

<a name="teststrategy"></a>
## Test Strategy

To ensure the site is fit for purpose all user stories and features documented in the main README.md file are to be tested. The test procedures
and results are documented below.

The code (HTML/CSS/JS/Python) must also satisfy the requirements of the online validation tools. These are:
* [W3C Markup Validation Service](https://validator.w3.org/). Check the markup of web documents.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Check Cascading Style Sheets
* [JS Hint](https://jshint.com/). Javascript code quality tool. 
* [PEP8 Online](http://pep8online.com/). Checks Python code for PEP8 compliance.

Google Lighthouse will be used to check the Performance, Accessibility, Best Practices and Search Engine Optimisation of the website.

<a name="userstorytesting"></a>
## User Story Testing

<a name="functionaltesting"></a>
## Functional/Features Testing

<a name="codevalidation"></a>
## Code Validation

### [PEP8 Online Check](http://pep8online.com/)

### [JS Lint](https://jslint.com/)
* Stripe Elements Java Script
    * Warnings reported by JS Lint. See report [here](docs/images/008 - StripJSLint.png).

### [W3C HTML Checker](https://validator.w3.org/nu/)
* Home Page
    * Errors & warnings reported for the Vinyl Rack Home page. See [here](docs/images/001-HomePageHTMLCheck.png) for details. 
    Modified the appropriate HTML and repeated the test - no errors found.

* Product Page
    * No errors reported

* Artist Page
    * No errors reported

* Genre Page
     * No errors reported

* Record Label Page
    * No errors reported

* Add Product Page
    * Errors & warnings reported for the Product Management Page. See [here](docs/images/002-ProductAddHTMLCheck.png) for details.
        * All the duplicate attributes and IDs were ignored as the duplicate items were on the modal forms and therefore separate from the main html. These errors did not impace on the performace/operation of the site. Maybe these should be addressed at a later date.
        * The error 'Element p not allowed as child of element strong in this context' seemed to be coming from the Crispy Forms so was ignored.

* Edit Product Page
    * Errors & warnings reported for the Product Management Page. See [here](docs/images/006-ProductEditPageHTMLCheck.png) for details.
        * The img alt atribute was added in the CustomClearableFileInput widget.
        * The error 'Element p not allowed as child of element strong in this context' seemed to be coming from the Crispy Forms so was ignored.

* My Profile Page
    * No errors reported

* My Wishlist Page
    * Errors & warnings reported for the Vinyl Rack Home page. See [here](docs/images/003-WishlistPageHTMLCheck.png) for details.
    Modified the appropriate HTML and repeated the test - no errors found.

* My Reviews Page
    * No errors reported

* Product Details Page
    * Errors & warnings reported for the Vinyl Rack Home page. See [here](docs/images/004-ProductDetailPageHTMLCheck.png) for details.
        * Removed code that was used during testing/development of the page. Repeated the test and no errors found.

* Add Review Page
    * Errors & warnings reported for the Vinyl Rack Home page. See [here](docs/images/005-AddReviewPageHTMLCheck.png) for details.
        * Added the missing action url to the form to fix the error. Repeated the test and no errors found.
    
* Edit Review Page
    * No errors reported

* Contact Us Page
    * No errors reported

* Shopping Bag Page
    * Errors & warnings reported for the Vinyl Rack Home page. See [here](docs/images/007-ShoppingBagPageHTMLCheck.png) for details.
        * The error 'Element p not allowed as child of element strong in this context' seemed to be coming from the Crispy Forms so was ignored.
        * The duplicate IDs are from the code used to generate different views for small and large screens. Different code will be rendered depending on the size of the screen. Errors ignored.

* Chekout Page
    * No errors reported

* Checkout Success Page
    * No errors reported

* Sign Out Page
    * No errors reported

* Sign In Page
    * No errors reported

* Registration Page
    * No errors reported

### [W3C CSS Checker](https://jigsaw.w3.org/css-validator/)

<a name="bugsissues"></a>
## Bugs / Issues
