## Testing

### Table of Contents

[Test Strategy](#teststrategy)

[Responsive Testing](#responsivetesting)

[User Story Testing](#userstorytesting)

[Functional/Features Testing](#functionaltesting)

[Code Validation](#codevalidation)

[Bugs / Issues](#bugsissues)

<a name="teststrategy"></a>
## Test Strategy

To test responsiveness of the site [Chrome DevTools](https://developer.chrome.com/docs/devtools/) will be used. This ensures the site is usable on a varitey of different devices and screen sizes.

To ensure the site is fit for purpose all user stories and features documented in the main README.md file are to be tested. The test procedures
and results are documented below.

The code (HTML/CSS/JS/Python) must also satisfy the requirements of the online validation tools. These are:
* [W3C Markup Validation Service](https://validator.w3.org/). Check the markup of web documents.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Check Cascading Style Sheets
* [JS Hint](https://jshint.com/). Javascript code quality tool. 
* [PEP8 Online](http://pep8online.com/). Checks Python code for PEP8 compliance.

Google Lighthouse will be used to check the Performance, Accessibility, Best Practices and Search Engine Optimisation of the website.

<a name="responsivetesting"></a>
## Responsive Testing

### Mobile & Tablet
The responsiveness of the site was tested using the Device Mode in [Chrome DevTools](https://developer.chrome.com/docs/devtools/). For mobile devices the minimum screen width the site was tested at was 320 pixels (iPhone SE). The following mobile and tablet options were tested in [Chrome DevTools](https://developer.chrome.com/docs/devtools/):

* Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro, Surface Duo, Nest Hub & Nest Hub Max

The responsiveness was also tested on an actual Samsung Galaxy S8 Plus and an iPhone 12 ProMax. The site was consistently resposive across all devices and screen sizes with the layout responding as expected.

### Desktop
The resposiveness of the site on desktop devices was tested using Chrome, Firefox, Edge, Opera and Safari browsers. The site was tested using the following screen widths:

* 1024 pixels, 1280 pixels, 1440 pixels, 1600 pixels and 1920 pixels.

The site was consistently resposive across all devices and screen sizes with the layout responding as expected.


<a name="userstorytesting"></a>
## User Story Testing

### New Users
* *"As a new user, I want a clear layout so I can easily navigate the site on all platforms."*
* *"As a new user, I would like view all records sold within the store without having to register for an account."*
* *"As a new user, I would like to see new releases and/or special offers on the Home page."*
* *"As a new user, I would like see all releases within a particular genre."*
* *"As a new user, I would like to see all releases by a particular artist/band."*
* *"As a new user, I would like the ability to search the store either by artist or album name."*
* *"As a new user, I would like to be able to add items to a shopping basket"*
* *"As a new user, I would like to be able to edit / delete items that are already in my shooping basket."*
* *"As a new user, I would like to clearly see the total cost of my order including any shipping costs."*

### Registered Users
* *"As a registered user, I would like to see my previous orders or the status of current orders."*
* *"As a registered user, I would like to save items to a wish list so I can keep track of potential future purchases."*
* *"As a registered user, I would like the option to save my delivery details so I don't need to keep enetering them."*
* *"As a registered user, I would like the ability write a review of a record sold on the site."*
* *"As a registered user, I would like the ability to edit or delete a previous review that I have left for a particular product."*
* *"As a registered user, I would like the ability to edit or delete my profile/account."*

### Returning Users
* *"As a returning user, I would like to easily see what new records have been added to the site."*
    * The 'New In' page displays the 8 most recent records added to the store. This page is accessible via the navigation bar at the top of the screen on desktop devices and in the burger menu on mobile devices.
* *"As a returning user, I would like to follow the record store on social media so I can stay updated on any upcoming events or new releases."*
    * Social media links are listed in the footer - these are visible on all pages.
* *"As a returning user, I would like to have the ability to contact the store if I have any questions or queries regarding a product or order."*
    * A 'Contact Us' link is available in the site footer. This is visible on all pages. Clicking on the link opens a page displaying a form that the user can complete to send any questions or quiries to the site admin.

### Store Owner / Administrator
* *"As the store owner / admin, I would like the ability to add records to the website."*
    * Records can be added to the site via the Product Management page. Once the user is logged in and has the correct permissions the Product Management page can be accessed via the My Account icon in the navigation bar.
* *"As the store owner / admin, I would like the ability to edit records on the website."*
    * When logged in as an admin the edit option for a record will be visibe on the products page and the product details page. Clicking on this link will open the edit product page.
* *"As the store owner / admin, I would like the ability to delete records from the website."*
    * When logged in as an admin the delete option for a record will be visibe on the products page and the product details page. Clicking on this link will open a modal for the to confirm delete of the item from the database.
* *"As the store owner / admin, I would like the ability to apply discounts to indiviual records."*
    * The product model has a boolean field 'on_sale' and when this is True the item will be marked for sale on the site. The percentage discount is entered in the 'discount_percent' field. These fields can be set when adding a new product to the site or when editing an existing product.
* *"As the store owner / admin, I would like the ability to apply site wide discounts for large sale events."*
    * Currently the only way to apply discounts to products is using the 'on_sale' and 'discount_percent' fields as described above. There is no method of providing site wide discounts but this could be added at a future date.
* *"As the store owner / admin, I would like the ability to tag items to appear in the home page."*
    * Currently the home page displays the last 8 items added to the database. The only way for the admin to tag an item for displaying on the home page is to modify the date added field. This isn't ideal but was deemed a suitable solution for this implementation/release of the site.
* *"As the store owner / admin, I would like the ability to edit or delete any user reviews if they breach the website guidelines."*
    * Site administrators can edit or delete any reviews via the Django admin console. This feature wasn't implemented on the main site as the admin console provides all the functionality that is required.

<a name="functionaltesting"></a>
## Functional/Features Testing

<a name="codevalidation"></a>
## Code Validation

### Python Flake8 Validation
* All python code was checked using Flake8. These results can be found [here](/docs/python-flake8-results.txt). A few of the errors relating to longer lines were not refactored as these were either auto generated files or determined to be of low importance.

### [PEP8 Online Check](http://pep8online.com/)
* All Python code was checked using the PEP8 online validation tool. No errors were found using the online tool and any warnings addressed as required.

### [JS Lint](https://jslint.com/)
* Stripe Elements Java Script
    * Warnings reported by JS Lint. See report [here](docs/images/008-StripJSLint.png).

* Country Field Java Scrip 
    * No errors reported

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
