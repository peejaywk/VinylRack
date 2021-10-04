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

### Test-001 : Navigation Bar
Test navigation bar links function correctly and that the correct links are displayed for admin and non admin users.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/. Logout of the site if logged in.
2. Check that the nav bar is fixed to the top of the browser window when scrolling down.
3. With the user logged out check that the following menu options appear in the the My Account drop down menu:
    * Register & Login
4. Click each of the menu options listed above and confirm that you are taken to the correct page.
5. Login as a regular non admin user and check that the following menu options appear in My Account drop down menu::
    * My Profile, My My Wishlist, My Reviews & Logout.
6. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the website.
7. Login in using an administrator account and check that the following options appear in the nav bar:
    * Product Management, My Profile, My My Wishlist, My Reviews & Logout
8. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the website.
9. On desktop devices confirm that clicking on the Vinyl Rack icon in the top left returns the user to the home page.
10. Confirm that all the navigation links under the Catalogue drop down menu function correclty. On mobile devices these will collapse into a hamburger icon.
11. Confirm that the New In and On Sale links function correclty. On mobile devices these will collapse into a hamburger icon.
12. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
13. Repeat the above steps using a mobile device if possible.
14. Repeat the above tests with a screen size of <=992 pixels and check that the menu options Catalogue, On Sale & New In collapse into the hamburger icon. Also confirm that the Vinyl Rack icon is not rendered and that instead there is a Home link in the hamburger menu.
15. On mobile devices confirm that the Search, My Account and Shooping Bag icons are rendered at the top of the screen and function correctly.

#### Test Notes
All the navigation links function correctly for all users and link to the correct pages. For screen sizes <=992 pixels the correct navigation links
collapse into the hamburger menu and function correctly. The nav bar also remains fixed to the top of the page on both desktop and mobile devices. 
    
Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-002 : Footer
Test footer links function correctly and that it scrolls with the page contents.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Check that the footer remains at the bottom of the screen even when very little content is present.
3. Check that the footer scrolls down when displaying a page with lots of content.
4. Click on the Contact Us link and conform that the Contact Us page is loaded.
5. Click on each social media link and verify it opens up the correct page in a new browser tab.
6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
7. Repeat the above steps using a mobile device if possible.

#### Test Notes
The footer is located at the bottom of the screen when little content is present and scrolls down when more content is added or when viewing a page with lots of content. The Contact Us option links to the correct page and all social media links are working and link to the correct pages, opening in a new tab.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-003 : Home Page
Test to check the Home Page is displaying the correct information and that the links in the Jumbotron function correctly. 

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Confirm that the jumbotron at the top of the page is displaying the welcome message at that the buttons function correctly.
3. Confirm that the last eight products added to the site are displayed on the page.
4. Click on any of the album images and confirm that the correct product details page is displayed.
5. Return to the home page and click on any of the album/artist links below the album image and confirm the correct product details page is displayed.
6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
7. Repeat the above steps using a mobile device if possible.

#### Test Notes
The jumbotron is displayed correctly on desktop and mobile devices and both links function correctly taking the user to the appropriate page. The last eight products are being displayed on the home page and clicking on either the image or item text takes the user to the correct product details page.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-004 : User Registration

### Test-005 : User Authentication

### Test-006 : User Sign-out

### Test-007 : Product List Page
Test to confirm all the products available on the site are listed on the products list page. Check that the image, artist, album name and price are clearly displayed and that and items marked as 'on_sale' are displaying the percentage discount and the adjusted price. Also confirm that the edit/delete links are displayed for each product when the use is logged in the admin access.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Logout of the site if currently logged in.
3. Click on the All Products link in the Catalogue dropdown menu. Confirm that all the products available on the site are listed on the page.
4. Confirm that the image, artist, album name and price are clearly displayed.
5. For items marked as 'on_sale' confirm the percentage discount is displayed and the price has been adjusted accordingly.
6. Click on any product and confirm the correct product details page is opened.
7. Navigate back to the All Products page and login as an administrator.
8. Confirm that the edit/delete links are present below each of the products.
9. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
10. Repeat the above steps using a mobile device if possible.

#### Test Notes
Clicking on the All Products link in the Catalogue dropdown opens the correct page with all the available products listed. Any items that are marked 'on_sale' have the correct percentage discount and price displayed. When logged out or logged in as a non-admin there are no edit/delete links displayed.
When logged in as a site admin the edit/delete links are displayed below each of the products (see image below).

![Test007-Image](/docs/images/Test-007a.png)

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-008 : Product Details Page
Test to confirm that the correct information is displayed on the Product Details page for logged out user, logged in (non-adim) and logged in (admin).

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Logout of the site if currently logged in.
3. On the home page click on any product to open the product details page. Confirm that the page displays the correct information for the product and that the edit/delete links are not visible next to the artist name.
4. Login to the site as a non admin and confirm that the edit/delete links are not visible next to the artist name.
5. Login to the site with admin access and confirm that the edit/delete links are present next to the artist name.
6. Click on the Grading Info link and check the Grading Guide page is opened.
7. Find a product with a review rating and confirm the correct number of stars are being rendered.
8. Click the Add To Bag button and confirm that the item has been added to your shopping bag.
9. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
10. Repeat the above steps using a mobile device if possible.

#### Test Notes
The Product Details page displays the correct information for logged out, logged in (non admin) and logged in (admin) users. See image below for showing the product details page for a logged in admin user. The correct number of rating stars is also being rendered for product being viewed (see image below)

![Test008Image](/docs/images/Test-008a.png)

Clicking on the Grading Info link opens the Grading Guide page.

Clicking the Add To Bag button successfully adds the product to the shopping bag as can be seen in the two images below:

![Test008Image](/docs/images/Test-008b.png)

![Test008Image](/docs/images/Test-008c.png)

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-009 : Browse By Genre
Test to confirm the products can be browsed/filtered by Genre.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Click on the By Genre link in the Catalogue dropdown menu. Confirm that all the Genres are listed on the page.
3. Click on any Genre and confirm that the correct products are displayed for that particular genre. 
4. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
5. Repeat the above steps using a mobile device if possible.

#### Test Notes
Clicking on the By Genre link opens up the correct page displaying a list (sorted alphabetically) of all the different Genres.
The correct products were being displayed when clicking on any of the listed genres.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-010 : Browse By Artist
Test to confirm the products can be browsed/filtered by Artist.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Click on the By Artist link in the Catalogue dropdown menu. Confirm that all the Artists are listed on the page.
3. Click on any Artist and confirm that the correct products are displayed for that particular artist. 
4. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
5. Repeat the above steps using a mobile device if possible.

#### Test Notes
Clicking on the By Artist link opens up the correct page displaying a list (sorted alphabetically) of all the different artists listed on the site.
The correct products were being displayed when clicking on any of the listed artists.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-011 : Browse By Record Label
Test to confirm the products can be browsed/filtered by Record Label.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Click on the By Label link in the Catalogue dropdown menu. Confirm that all the Record Labels are listed on the page.
3. Click on any Record Label and confirm that the correct products are displayed for that particular Record Label. 
4. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
5. Repeat the above steps using a mobile device if possible.

#### Test Notes
Clicking on the By Label link opens up the correct page displaying a list (sorted alphabetically) of all the different record labels listed on the site.
The correct products were being displayed when clicking on any of the listed record labels.

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-012 : On Sale Page / Items
Test to confirm that the correct products are displayed on the On Sale page with the % discound and the price adjusted accordingly.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Click the On Sale link in navigation bar and confirm that the correct products are displayed. Only products with the 'on_sale' flag set should be displayed.
3. Confirm that the percentage discount is displayed below each image and that the unit price has been reduced correctly.
4. Click on any of the products to view the product details page.
5. Confirm that the percentage discount is displayed along with the discount price and original price.
6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
7. Repeat the above steps using a mobile device if possible

#### Test Notes
The On Sale page displayed all products that had the 'on_sale' flag set True. The currect percentage discount was visible below the image and the price had been reduced by the correct amount (see image below).

![Test-011-Image](/docs/images/Test-011b.png)

The product details page for a sale item displayed the correct percentage discount along with the correct sale price and original price (see image below).

![Test-011-Image](/docs/images/Test-011a.png)

Tests performed using  Chrome, Firefox, Opera, Edge & Safari desktop browsers.
Repeated tests using a Samsung Galaxy S8 mobile device with no issues.

#### Test Results
* **PASS**

### Test-013 : New In Page
Test to confirm the last eight products added to the site are displayed on the New In page.

1. Open Chrome browser and navigate to: https://vinyl-rack.herokuapp.com/.
2. Click the New In link in navigation bar and confirm that the last eight products added to the site are displayed.
3. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
4. Repeat the above steps using a mobile device if possible

#### Test Notes
Clicking on the New In link on the navigation bar displayed the correct items on the new in page. These were confirmed to be the last eight products added to the site.

#### Test Results
* **PASS**

### Test-014 : Add New Product

### Test-015 : Edit Product

### Test-016 : Delete Product

### Test-017 : Add to Wishlist

### Test-018 : Remove from Wishlist

### Test-019 : Add Review

### Test-020 : Edit Review

### Test-021 : Delete Review

### Test-022 : Add/Remove/Delete to/from Cart

### Test-023 : Checkout Strip Payment

### Test-024 : Profile Page

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
