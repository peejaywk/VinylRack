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

### Frontend Design
The [Bootstrap](https://getbootstrap.com/) framework was used to implement the frontend of the website to give a responsive design that provides a good UX across all devices and screen sizes.

### Icons
[Font Awesome](https://fontawesome.com/) has been used throughout this project to provide any icons that are required.

### Colour Scheme
A neutral colour scheme was chosen for the site as most of the color on majority of pages is provided by the album artwork. A simple black and white theme was chosen with a light green colour being used for the delivery details banner and to display the discount percentage when required.

* ![#4D724D](https://via.placeholder.com/15/4D724D/000000?text=+) #4D724D
    * Delivery details banner
    * Footer background colour
    * Percentage discount badge background colour
* A custom black button was created and used throughout the site - otherwise the default Bootstrap colours were used for buttons

<a name="features"></a>
## Features

### Common Features Across ALL Pages
* Header
    * The header will be in a fixed position at the top of the screen and will not scroll with the page contents. This allows visitors easy access to navigate the site via the menu.
    * The header will include a nav bar split into two rows.
        * The top row will include a link back to the home page, a search bar and links to My Accounts and the Shopping Cart.
        * The bottom section will include another navigation menu, aligned to the left of the page, that includes links to allow the user to browse the shop by Genre, Artist or Label and also to view new or sale items in the store.
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

The database schema was captured using [DrawSQL](https://drawsql.app/) and can be viewed [here](/docs/drawSQL-export-2021-10-04_09_49.png).

### Profile App

#### User Profile Model

Note: For the user model in the Profile App the Django Allauth and its `django.contrib.auth.models` was used.

|Name             |Database Key            |Field Type         | Validation Requirements                     |
|-----------------|------------------------|-------------------|---------------------------------------------|
|User             |user                    |OneToOneField(User)|on_delete=models.CASCADE                     |
|Phone Number     |default_phone_number    |CharField          |max_length=20, null=True, blank=True         |
|Street Address 1 |default_street_address1 |CharField          |max_length=80, null=True, blank=True         |
|Street Address 2 |default_street_address2 |CharField          |max_length=80, null=True, blank=True         |
|Town or City     |default_town_or_city    |CharField          |max_length=40, null=True, blank=True         |
|County           |default_county          |CharField          |max_length=80, null=True, blank=True         |
|Postcode         |default_postcode        |CharField          |max_length=20, null=True, blank=True         |
|Country          |default_country         |CountryField       |blank_label='Country', null=True, blank=True |

### Products App

#### Genre Model
|Name             |Database Key  |Field Type | Validation Requirements              |
|-----------------|--------------|-----------|--------------------------------------|
|Name             |name          |CharField  |max_length=254                        |
|Friendly Name    |friendly_name |CharField  |max_length=254, null=True, blank=True |

#### Artist Model
|Name             |Database Key  |Field Type | Validation Requirements              |
|-----------------|--------------|-----------|--------------------------------------|
|Name             |name          |CharField  |max_length=254                        |
|Friendly Name    |friendly_name |CharField  |max_length=254, null=True, blank=True |

#### Recordlabel Model
|Name             |Database Key  |Field Type | Validation Requirements              |
|-----------------|--------------|-----------|--------------------------------------|
|Name             |name          |CharField  |max_length=254                        |
|Friendly Name    |friendly_name |CharField  |max_length=254, null=True, blank=True |

#### Product Model
| Name             | Database Key            | Field Type              | Validation Requirements                              |
|------------------|-------------------------|-------------------------|-------------------------------------------------------|
| Sku              | sku                     | CharField               | max_length=254, default="", blank=True                |
| Genre            | genre                   | ForeignKey(Genre)       | null=True, blank=True, on_delete=models.SET_NULL      |
| Artist           | artist                  | ForeignKey(Artist)      | null=True, blank=True, on_delete=models.SET_NULL      |
| Record Label     | record_label            | ForeignKey(Recordlabel) | null=True, blank=True, on_delete=models.SET_NULL      |    
| Album Title      | album_title             | CharField               | max_length=254                                        |    
| Description      | description             | TextField               | None                                                  |        
| Price            | price                   | DecimalField            | max_digits=6, decimal_places=2                        |    
| On Sale          | on_sale                 | BooleanField            | default=False, blank=True                             |
| Discount Percent | discount_percent        | DecimalField            | max_digits=2, decimal_places=0, blank=True, null=True |
| Image            | image                   | ImageField              | null=True, blank=True                                 |
| Image Url        | image_url               | URLField                | max_length=1024, default="", blank=True               |
| Media Condition  | media_condition         | CharField               | max_length=16                                         |
| Sleeve Condition | sleeve_condition        | CharField               | max_length=16                                         |   
| Calalogue Number | cat_num                 | CharField               | max_length=254, default="", blank=True                |   
| Date Added       | date_added              | DateTimeField           | default=timezone.now                                  |
    
### Checkout App

#### Order Model
| Name                     | Database Key    | Field Type                 | Validation                                                   |
| ------------------------ | --------------- | ---------------------------| -------------------------------------------------------------|
| Order Number             | order_number    | CharField                  | max_length=32, null=False, editable=False                    |
| User Profile             | user_profile    | ForeignKey(UserProfile)    | on_delete=models.SET_NULL, null=True, related_name='orders'  |
| Full Name                | full_name       | CharField                  | max_length=50, null=False, blank=False                       |
| Email Address            | email           | EmailField                 | max_length=254, null=False, blank=False                      |
| Phone Number             | phone_number    | CharField                  | max_length=20, null=False, blank=False                       |
| Country                  | country         | CountryField               | blank_label='Country *', null=False, blank=False             |
| Postcode                 | postcode        | CharField                  | max_length=20, null=True, blank=True                         |
| Town or City             | town_or_city    | CharField                  | max_length=40, null=False, blank=False                       |
| Street Address 1         | street_address1 | CharField                  | max_length=80, null=False, blank=False                       |
| Street Address 2         | street_address2 | CharField                  | max_length=80, null=True, blank=True                         |
| County                   | county          | CharField                  | max_length=80, null=True, blank=True                         |
| Date                     | date            | DateTimeField              | auto_now_add=True                                            |
| Delivery Cost            | delivery_cost   | DecimalField               | max_digits=6, decimal_places=2, null=False, default=0        |
| Order Total              | order_total     | DecimalField               | max_digits=10, decimal_places=2, null=False, default=0       |
| Grand Total              | grand_total     | DecimalField               | max_digits=10, decimal_places=2, null=False, default=0       |
| Original Bag             | original_bag    | TextField                  | null=False, blank=False, default=''                          |
| Stripe Payment Intent ID | stripe_pid      | CharField                  | max_length=254, null=False, blank=False, default=''          |

#### Order Line Item Model
| Name            | Database Key   | Field Type          | Validation                                                                   |
| --------------- | -------------- | --------------------| -----------------------------------------------------------------------------|
| Order           | order          | ForeignKey(Order)   | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'  |
| Product         | product        | ForeignKey(Product) | null=False, blank=False, on_delete=models.CASCADE                            |
| Quantity        | quantity       | IntegerField        | null=False, blank=False, default=0                                           |
| Line Item Total | lineitem_total | DecimalField        | max_digits=6, decimal_places=2, null=False, blank=False, editable=False      |

### Wishlist App

#### Wishlist Model
| Name            | Database Key   | Field Type               | Validation                                                                   |
| --------------- | -------------- | -------------------------| -----------------------------------------------------------------------------|
| User            | user           | OneToOneField(User)      | on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist'   |
| Products        | products       | ManyToManyField(Product) | through='WishlistItem', related_name='wishlist_products'                     |

#### Wishlist Item Model
| Name            | Database Key   | Field Type           | Validation                                         |
| --------------- | -------------- | ---------------------| ---------------------------------------------------|
| Wishlist        | wishlist       | ForeignKey(Wishlist) | null=False, blank=False, on_delete=models.CASCADE  |
| Product         | product        | ForeignKey(Product)  | null=False, blank=False, on_delete=models.CASCADE  |
| Date Added      | date_added     | DateTimeField        | default=timezone.now                               |

### Review App

#### Review Model
| Name            | Database Key   | Field Type           | Validation                                                                |
| --------------- | -------------- | ---------------------| --------------------------------------------------------------------------|
| User            | User           | ForeignKey(User)     | on_delete=models.CASCADE, null=False, blank=False, related_name='review'  |
| Product         | product        | ForeignKey(Product)  | on_delete=models.CASCADE, null=False, blank=False, related_name='product' |
| Created On      | created_on     | DateTimeField        | default=timezone.now                                                      |
| Review Rating   | review_rating  | IntegerField         | default=4                                                                 |
| Review Title    | review_title   | CharField            | max_length=254, null=False, blank=False                                   |
| Review Content  | review_content | DateTimeField        | max_length=1200, null=False, blank=False, default=''                      |

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
* [Heroku](https://heroku.com)


<a name="testing"></a>
## Testing

See [testing.md](/assets/documentation/testing.md) for the testing documentation.

<a name="deployment"></a>
## Deployment

This project was developed using [GitPod](https://gitpod.io/) and the latest version of the code base can be found in the master branch of this
repository. No other branches were created during the development of this project.

### Cloning the Repository

To clone this [repository](https://github.com/peejaywk/VinylRack) follow the instruction below:

1. Navigate to the [repository](https://github.com/peejaywk/VinylRack).

2. Click on the **Code** button and copy the URL from the **Clone>>HTTPS** section.

3. Inside your development environment/IDE open a command terminal.

4. Create / navigate to the directory you would like the cloned copy to be made.

5. Type in the following command using the URL copied from step 2 and press Enter. This will create a cloned copy of the repository.

        git clone https://github.com/peejaywk/VinylRack

### Deploying to Heroku from Gitpod

1. Open [Heroku](https://heroku.com) in the browser and login creating a new account if required.
2. On the Heroku Dashboard click New->Create New App.
3. Give the app a new name and choose a region closest to you. Click the Create App button.
4. On the resource tab provision a new Postgres database selecting the free Hobby Dev plan.
5. To use Postgres in the application two packages are required - these are dj-database-url and psycopg2. To install these in Gitpod type the following commands:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2-binary`
6. Freeze the requirements in Gitpod by typing `pip3 freeze > requirements.txt`. Heroku will use the requirements.txt file to install these packages during deployment.
7. Open the settings.py file and import the dj_database_url package by adding `import dj_database_url` at the top of the file underneath `import os`.
8. In the database section comment out the default configuration and replace with the code below. The DATABASE_URL can be found under the settings tab in Heroku in the Config Vars section.

```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
    }
```
9. As a new database has been connected the migrations will need to run again to setup the database. Type in the following commands in Gitpod to run the migrations.
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
10. The database can be populated using the fixtures and JSON files. Run the following commands to load the data into the Postgres database:
    * `python3 manage.py loaddata genres`
    * `python3 manage.py loaddata artists`
    * `python3 manage.py loaddata record_labels`
    * `python3 manage.py loaddata products`
11. Create a superuser account for Django Administrator Panel using command `python3 manage.py createsuperuser`. When prompted enter a username, email address and password.
12. To ensure the database URL doesn't end up in version control replace the database configuration as setup in step 8 with the code below. When running on Heroku the DATABSE_URL will be defined in the Config Vars and the correct URL will be parsed by dj_database_url. Otherwise the sqlite database will be used when running in the Gitpod development environment.
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
```
13. For the app to run the Gunicorn webserver package is required. To install this package run command `pip3 install gunicorn`.
14. Freeze the requirements by running command `pip3 freeze > requirements.txt`.
15. In the root directory of the project create a Procfile by running command `touch Procfile`. The Procfile is used to tell Heroku to create a web dyno to run gunicorn and serve our Django app.
16. Open the Procfile copy in the following text ensuring there is no blank line at the end of the file.
```
    web: gunicorn vinylrack.wsgi:application
```
17. Login to Heroku using the `heroku login -i` command.
18. As AWS will be used to host the static files we need to prevent Heroku from collecting static files during deployment. This can be done by setting DISABLE_COLLECTSTATIC to 1. Enter the following command to set DISABLE_COLLECTSTATIC:
    * `heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name`
19. In the settings.py file add the Heroku app the list of allowed hosts. Also add in localhost to ensure the app still works in Gitpod.
    * `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`
20. Edit the .gitignore file (or create a new one if it doesn't exist) and add the following if required:
```
    core.Microsoft*
    core.mongo*
    core.python*
    env.py
    __pycache__/
    *.py[cod]
    node_modules/
    .github/
    *.sqlite3
    *.pyc
```
21. Commit the changes to the main Github repository using the following commands:
    * `git add .`
    * `git commit -m "Add commit message here"`
    * `git push`
22. Initialise the Heroku repository using command `heroku git:remote -a app-name`.
23. To deploy the app to Heroku push the changes to the remove Heroku repository using command `git push heroku main`. This will deploy the site without any static files.
24. To automatically deploy when any changes are committed to Github click in the Deploy tab in Heroku and set the Deployment method to Github.
25. In the Connect to GitHub section search for the repository and click connect when the correct one is found.
26. In the Automatic Deploys section click on the Automatic Deplots button. This ensures that every time we push any changes to Github the code will be automatically be deployed to heroku as well.
27. Create a new Django secret key using the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) website.
28. In Heroku under the Settings tab create a new Config Var with a key name of SECRET_KEY with the value set to the key generated in the previous step.
29. To ensure the Heroku app picks up this key add the following to the settings.py file:
    * `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
30. Commit the changes to Github. Heroku should pickup the changes from Github and deploy the site to app-name.herokuapp.com.


<a name="credits"></a>
## Credits
* [Filling Star Ratings: George Martsoukos](https://webdesign.tutsplus.com/tutorials/a-simple-javascript-technique-for-filling-star-ratings--cms-29450)
* [Jumbotron Image](https://unsplash.com/photos/CbNBjnXXhNg) Unsplash Credit @rocinante_11
* Standard record grading text copied from [Vinyl Music Madness](https://vinylmusicmadness.co.uk/record-collector-grading)