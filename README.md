# Vinyl Rack

Vinyl Rack is an online store selling new and second hand vinyl records. The website allows users to browse/search items available in the store and to purchase then using a secure payment system. By registering for an account users can leave ratings/reviews for records sold in the store and also add items to their own wish list. Delivery details can also be stored within a users profile making checkout easier for future orders.

New records will be clearly displayed on the Home page allowing returning users/customers to see what records have been added to the store.


## Table of Contents

[User Experience (UX)](#userexperience)

[Features](#features)

[Database Design](#database)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

<a name="userexperience"></a>
## User Experience (UX)

### Objectives
* Provide a modern responsive website where users can easily browse/find records.
* Provide a simple way for users to add items to their shopping basket.
* Provide a secure means of purchasing items from the store.
* Allow users to leave ratings/reviews for records available in the store.
* Encourage users to register with the site to activate their wishlist and to store delivery information.
* To allow future expansion to include different genres / artists and media (such as CD, cassettes)

### User Stories
#### New Users
* As a new user, I want a clear layout so I can easily navigate the site on all platforms.
* As a new user, I would like view all records sold within the store without having to register for an account.
* As a new user, I would like to see new releases and/or special offers on the Home page.
* As a new user, I would like see all releases within a particular genre.
* As a new user, I would like to see all releases by a particular artist/band.
* As a new user, I would like the ability to search the store either by artist or album name.
* As a new user, I would like to be able to add items to a shopping basket
* As a new user, I would like to be able to edit / delete items that are already in my shooping basket.
* As a new user, I would like to clearly see the total cost of my order including any shipping costs.

#### Registered Users
* As a registered user, I would like to see my previous orders or the status of current orders.
* As a registered user, I would like to save items to a wish list so I can keep track of potential future purchases.
* As a registered user, I would like the option to save my delivery details so I don't need to keep enetering them.
* As a registered user, I would like the ability write a review of a record sold on the site.
* As a registered user, I would like the ability to edit or delete a previous review that I have left for a particular product.
* As a registered user, I would like the ability to edit or delete my profile/account.

#### Returning Users
* As a returning user, I would like to easily see what new records have been added to the site.
* As a returning user, I would like to follow the record store on social media so I can stay updated on any upcoming events or new releases.
* As a returning user, I would like to have the ability to contact the store if I have any questions or queries regarding a product or order.

#### Store Owner / Administrator
* As the store owner / admin, I would like the ability to add records to the website.
* As the store owner / admin, I would like the ability to edit records on the website.
* As the store owner / admin, I would like the ability to delete records from the website.
* As the store owner / admin, I would like the ability to apply discounts to indiviual records.
* As the store owner / admin, I would like the ability to apply site wide discounts for large sale events.
* As the store owner / admin, I would like the ability to tag items to appear in the home page.
* As the store owner / admin, I would like the ability to edit or delete any user reviews if they breach the website guidelines.

### Wireframe Mockups
The initial wireframe mockups for the website are linked below. These initial designs were captured using [Balsamiq](https://balsamiq.com/).

* [Home Page](/docs/wireframes/001-HomePage-v1.png)
* [Product List Page](/docs/wireframes/002-ProductListPage-v1.png)
* [Product Page](/docs/wireframes/003-ProductPage-v1.png)
* [Shopping Bag Page](/docs/wireframes/004-ShoppingBagPage-v1.png)
* [Checkout Page](/docs/wireframes/005-CheckoutPage-v1.png)
* [Wishlist Page](/docs/wireframes/006-WishListPage-v1.png)
* [Profile Page](/docs/wireframes/007-ProfilePage-v1.png)
* [Product Management Page](/docs/wireframes/008-ProductManagementPage-v1.png)
* [Contact Page](/docs/wireframes/009-ContactPage-v1.png)

<a name="features"></a>
## Features

### Common Features Across ALL Pages
* Header
    * The header will be in a fixed position at the top of the screen and will not scroll with the page contents. This allows visitors easy access to navigate the site via the menu.
    * The header will include a nav bar split into two rows.
        * The top row will include a link back to the home page, a search bar and links to My Accounts and the Shopping Cart.
        * The bottome section will include another navigation menu, aligned to the left of the page, that includes links to allow the user to browse the shop by Genre, Artist or Label and also to view new or sale items in the store.
    * On mobile the navigation links in the bottom row will collapse into a burger menu. The links to My Account and Shopping Cart will remain visibale at the top of the screen for easy access.
    * The navigation links in the My Account dropdown will change when the user is registered and logged in.
    * A message bar will be positioned below the header to allow information to be presented to the user.
* Footer
    * The footer will be located at the bottom of each page and will scroll with the page contents.
    * A disclaimer will be positioned in the footer stating that this website is for educational purposes only.
    * Social media links and other contact information will be positioned to the right of the footer.
    * Social media links will be represented by icons for each site and will increase when the user hovers over them.
    * There will be a contact link at the bottom of the page that will take the user to the contact page.
* Home Page
    * The Home page will clearly display products that have been recently added to the website. The album artwork will the main feature on the Home page with artist/album title and price displayed under each image.
    * At the top of the page there will be quick links that will allow the user to view all new products, products on sale or all products on the site.
    * Clicking on the album image will open up a new page containing more details on the selected product.
    * The layout/size of the album images will be responsive and will resize for different screen sizes. On mobile devices the albums will be presented in a single column to maximise the image size.
* Product List Page
    * The Product List page will display a list of all the products available on the site or the products from a particular category. This could be genre, artist, sale items etc.
    * The page will clearly display the album image, artist name, album title, price and a description of the product. 
    * Clicking on the album image will open up a new page containing more details on the selected product.
    * If the user has administrator privileges and is logged in then there will be addition links on each item allow the user to edit/delete the product.
    * On mobile devices the detailed description will not be displayed to stop the page becoming too cluttered.
    * A link to the product reviews (if any) will be displayed next to each product. If a user is logged in then they will be able to leave a product review/rating.
* Product Page
    * This will display all data associated with a particular product. There will be buttons to allow the user to add the product to their shopping basket or wish list of they have created an account and are logged in.
    * If the user has administrator privileges and is logged in then there will be addition links on each item allow the user to edit/delete the product.
    * A link to the product reviews (if any) will be displayed next to each product. If a user is logged in then they will be able to leave a product review/rating.
* Shopping Bag Page
    * The shopping bag will display all items that that have been added by the user.
    * For each item it will show the unit price, quantity and subtotal.
    * The user can change the quanity against each item and also remove it from their back if they no longer wish to purchase the product.
    * At the bottome of the page the basket total, delivery cost and order total will be displayed. On mobile screens this will be positioned at the top of the screen so the user can easily see the total cost of their order.
    * A Keep Shopping anf Checkout button will also be displayed at the bottom of the page.
* Checkout Page
    * The Checkout page will contain a bried summary of the order and a form for the delivery details.
    * If the user is logged in then the form will be populated with any address information the user has saved in their profile.
    * The form will be validated on submission and any errors/ommissions will be reported back to the user.
    * The payment information system will be implemented by Stripe and it will allow the user to enter a card number, expirey date and CVC number.
    * Buttons at the bottom of the page will allow the user to complete the order or adjust the order.
* Profile Page
    * Once a user is registered they will have access to their profile page. This allows the user to enter default delivery information, view previous orders and view/edit/delete any reviews they have written on the site.
* Product Management Page
    * Site administrators can use this page to add new products to the website and also edit existing products in the database.
* Wish List Page
    * Registered users will have the ability to add products to their wishlist. The wish list page will be accessible via the My Account dropdown in the nav bar and will display all items in their wish list.
    * Items from the wish list can be deleted or added to the users shopping cart.

<a name="database"></a>
## Database Design
During development the website will use SQLite3 which is the default database used by Django. Once deployed the website will use a PostgreSQL database which can be added/hosted by Heroku.

The database schema was captured using [DrawSQL](https://drawsql.app/) and can be viewed [here](/docs/drawSQL-export-2021-08-22_14_40.png).

<a name="technologies"></a>
## Technologies Used

### Languages
* This website uses HTML, CSS, JavaScript & Python programming languages.

### Libraries & Frameworks
* [Font Awesome](https://fontawesome.com/)
* [Googel Fonts](https://fonts.google.com/)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/)
* [Django](https://www.djangoproject.com/)

### Tools
* [Balsamiq](https://balsamiq.com/)
* [DrawSQL](https://drawsql.app/)
* [GitPod](https://gitpod.io/)
* [GitHub](https://github.com/)


<a name="testing"></a>
## Testing

Images not being displayed on the wishlist page on screen sizes above medium.
Incorrect bootstrap class applied. Changed from 'd-none d-md-cell' to 'd-none d-md-table-cell' which fixed the issue.

<a name="deployment"></a>
## Deployment

<a name="credits"></a>
## Credits
* [Filling Star Ratings: George Martsoukos](https://webdesign.tutsplus.com/tutorials/a-simple-javascript-technique-for-filling-star-ratings--cms-29450)