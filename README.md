# Pet Store and More e-Comerce Website

This e-comerce website is created because of love towards our fury family members.
The goal of this website is to help pet owners to buy all the things necessary for their beloved pets.
The website is designed in a way to ease the process of buying all the things needed.
This website is sutable for all age levels.
Visitor should be able to:
- Register
- Login
- Logout
- Add\Update personal information
- Access shopping cart
- Browse all products on the website
- Browse all products based on Price, Rating, and Category
- Browse all pet specific products
- Browse specific product type of specific pet type
- Manage entries (update\delete) if given Administrator permissions
- Inspect items in Shopping cart (add/remove/update count if necessary)
- Enter billing information during checkout process
- Receive a confirmation email with purchase information

# <p align="center">[Pet Store and More e-Comerce Website Link](https://pet-store-and-more.herokuapp.com/ "Pet Store and More")</p>

## User Experience

### Plan

As someone who has a pet in the family, and where the pet is treated as an equal family member, I understand the struggles when you cannot find everything on one place.
This is why this website is created. The main purpose of this website is to provide all the necessary and essential products, together with other useful things to keep your pet happy and safe.

### User Stories

Reason why creating this website:

- be a place where visitor can create their profile by registering 
- be a place where visitor can login, and update its personal details (for the billing and shipping purposes)
- be a place where visitors can look for specific items for their pets
- be a place where visitors can look for new deals, clearance items, and discounted items
- be a place where visitors can search for a specific item
- be a place where visitor can at any time look at its purchase history and possibly re-order

## Wireframes

I used [AdobeXD](https://www.adobe.com/ie/products/xd.html) to create
[wireframes](https://github.com/vladimir-cmd/pet_store_and_more/tree/master/wireframes-mockups) in: 
[Front Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Default_View_Front_Page.png), 
[Register Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Register_Desktop.png),
[Signin Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/SignIn_Desktop.png),
[User Profile Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Profile_Desktop.png), 
[All Products Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/All_Products_Desktop.png), 
[Product Page](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Product_Desktop.png), 
[Products Per Pet Entry](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Products_Per_Pet_Desktop.png)
[Shopping Bag](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/wireframes-mockups/Shopping_Bag_Desktop.png)

## Features

### Page Features:

- [Home](https://pet-store-and-more.herokuapp.com/)
  - Home page contains a landing page where user can login or register.
  - Navigation bar where user can browse thru all products or narow down by selecting a specific type of an item.
  - User can search for a specific product by entering a keyword in searchfield.
  - User can directly go to all items page by clicking a 'shop now' button.

- [Profile](https://pet-store-and-more.herokuapp.com/profile/)
  - Profile page contains information about user and current order history.
  - User can search for a specific product by entering a keyword in searchfield.
  - User can update the following:
    - Phone Number
    - Country
    - Street Address
    - Town or City
    - Aircode
    - County

- [Product Management - Admin only](https://pet-store-and-more.herokuapp.com/products/add/)
  - Special section for Admins only where users with specific permissions can Add a Product.
  - User can search for a specific product by entering a keyword in searchfield.
  - User can specify the following:
    - Category
    - SKU
    - Name (Mandatory)
    - Description (Mandatory)
    - Has Sizes
    - Price (Mandatory)
    - Rating
    - Image URL
  
- [Products](https://pet-store-and-more.herokuapp.com/products/)
  - On this page user can see all the Products.
  - User can search for a specific product by entering a keyword in searchfield.
  - User can further choose from the following:
    - Select All Products dropdown menu
      - By Price
      - By Rating
      - By Category
    - Select Dog
      - Dry Dog Food
      - Wet Dog Food
      - Dog Treats
      - Dog Toys
      - Dog Beds
      - Dog Supplements
      - All Dog
    - Select Cat
      - Dry Cat Food
      - Wet Cat Food
      - Cat Toys
      - Cat Beds
      - Cat Supplements
      - All Cat
    - Select Birds
      - Bird Snacks
      - Bird Food
      - Bird Cages
      - Bird Toys
      - All Birds
    - Select Special Offers
      - New Items
      - Deals
      - Clearance
      - All Specials
  - User can further sort items by:
    - Price (low to high)
    - Price (high to low)
    - Rating (low to high)
    - Rating (high to low)
    - Name (A-Z)
    - Name (Z-A)
    - Category (A-Z)
    - Category (Z-A)

- [Product](https://pet-store-and-more.herokuapp.com/products/<item_id>)
  - User can search for a specific product by entering a keyword in searchfield.
  - On this page user can see Product information such as:
    - Name
    - Description
    - Price
    - Category
    - Rating
    - Admin Only:
      - Edit
      - Delete
  - User can further choose from the following:
    - Size
    - Quantity
    - Add to bag

- [Edit Item - Admin only](https://pet-store-and-more.herokuapp.com/products/edit/<entry_id>)
  - If user has Administrator permissions, it can delete the product by clicking on 'Edit' button
  - User can search for a specific product by entering a keyword in searchfield.
  - User can Update the following:
    - Category
    - Name
    - Description
    - Has Sizes
    - Price
    - Rating
    - Image URL
    - Select Image

- [Delete Item - Admin Only](https://pet-store-and-more.herokuapp.com/products/)
  - If user has Administrator permissions, it can delete the product by clicking on 'Delete' button
  - User can search for a specific product by entering a keyword in searchfield.

- [Shopping Bag](https://pet-store-and-more.herokuapp.com/bag/)
  - User can search for a specific product by entering a keyword in searchfield.
  - User can inspect content of the shopping bag
  - User can further update each item in the shopping bag with the following:
    - Quantity
    - Remove from shopping bag

- [Checkout](https://pet-store-and-more.herokuapp.com/checkout/)
  - User can search for a specific product by entering a keyword in searchfield.
  - User can have an overview of the shopping bag under 'Order Summary' section.
  - User can complete the order by filling out the following:
    - Name (Mandatory)
    - Email Address
    - Phone Number
    - Country
    - Postal Code
    - Town or City
    - Street Address 1
    - Street Address 2
    - County or State
    - Card number details

- [Register](https://pet-store-and-more.herokuapp.com/accounts/signup/)
  - Future user can register by entering the following:
    - Email Address
    - Confirm Email Address
    - Username
    - Password
    - Confirm Password
  - Password must match
  - Email Address must match
  - Username must be unique
  

- [Login](https://pet-store-and-more.herokuapp.com/accounts/login/)
  - User must provide username and password

## Technologies Used

In this project the following technologies have been used.

#### Database
- [PostgreSQL](https://www.postgresql.org/) 
  
  - production database, provided by heroku.

- [SQlite3](https://www.sqlite.org/index.html) 

  - development database, provided by django.

#### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)

  - Semantic markup language as the shell of the site.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - Programming language for the workability of the site.
  
#### Tools
- [FontAwesome](https://fontawesome.com/)

  - **FontAwesome** provided the icons used on the page.

- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

- [AWS S3 Bucket](https://aws.amazon.com/) 
  
  - store images entered into the database.

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 

  - enable creation, configuration and management of AWS S3.
  
- [Python Django](https://www.djangoproject.com/)

  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) 

  - style django forms.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) 

  - handle register, log in, log out, password recovery actions.

- [Gunicorn](https://pypi.org/project/gunicorn/) 

  - WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.

- [Pillow](https://pillow.readthedocs.io/en/stable/) 

  - python imaging library to aid in processing image files to store in database.

- [Psycopg2](https://pypi.org/project/psycopg2/) 

  - PostgreSQL database adapter for Python.

- [PIP3](https://pip.pypa.io/en/stable/) 

  - installation of tools needed in this project.

- [Stripe](https://stripe.com/en-ie) 
  
  - payment platform to validate and accept credit card payments securely.

- [Visual Studio Code](https://code.visualstudio.com/)

  - IDE (Integrated Development Environment).

- [IntelliJ Idea Community Edition](https://www.jetbrains.com/idea/)

  - IDE (Integrated Development Environment).

- [GitHub](github.com/)

  - The remote hosting platform.

- [Git](https://git-scm.com/) 

  - handle version control.

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - To see visually the elements of what each code produced, what happens if code is changed, and responsiveness of different device sizes.

- [Jigsaw](https://jigsaw.w3.org/css-validator)

  - To check for any errors in the CSS code.

## Testing

Testing information is found on a separate file [TESTING.MD](https://github.com/vladimir-cmd/pet_store_and_more/blob/master/TESTING.md)

## Deployment
### Run this project locally
To run this project on your own IDE follow the instructions below:
+ Tools which must be installed on your local machine: 
  - An IDE such as 
    - [Visual Studio Code](https://code.visualstudio.com/)
    - [IntelliJ](https://www.jetbrains.com/idea/download/#section=windows)

+ Software which must be installed on your local machine: 
  - [Python 3](https://www.python.org/downloads/)
  - [PIP](https://pip.pypa.io/en/stable/installing/)
  - [Git](https://git-scm.com/downloads)

+ Ensure you have created free accounts with the following services: 
  - [Stripe](https://stripe.com/en-ie) 
  - [AWS](https://aws.amazon.com/)
  - [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

#### Instructions
01. Save a copy of the github repository located at [Pet Store and More](https://github.com/vladimir-cmd/pet_store_and_more.git) by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. Much easier way is to just clone the repo with Git:
```
git clone https://github.com/vladimir-cmd/pet_store_and_more.git
```
02. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.
03. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```
04. Activate the .venv with the command:
```
.venv\Scripts\activate
```
05. Install all required modules with the command:
```
pip -r requirements.txt
```
06. Set up the following environment variables within your IDE.
+ If using VSCode, locate the settings.json file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them:
```
 "terminal.integrated.env.windows": {
    "HOSTNAME": "<enter hostname here>",
    "AWS_ACCESS_KEY_ID": "<enter key here>",
    "AWS_SECRET_ACCESS_KEY": "<enter key here>",
    "DATABASE_URL": "<enter key here>",
    "EMAIL_HOST_PASS": "<enter key here>",
    "EMAIL_HOST_USER": "<enter url here>",
    "SECRET_KEY": "<enter url here>",
    "STRIPE_PUBLIC_KEY": "<enter key here>",
    "STRIPE_SECRET_KEY": "<enter key here>",
    "STRIPE_WH_SECRET": "<enter key here>",
    "USE_AWS": "True",
    "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>"
 }
 ```
+ HOSTNAME should be the local address for the site when running within your own IDE.
07. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.
08. Migrate the admin panel models to create your database template with the terminal command:
```
python manage.py migrate
``` 
09. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
```
python manage.py migrate
```
10. You can now run the program locally with the following command:
```
python manage.py runserver
```
### Heroku Deployment
To deploy Pet Store and More webshop to heroku, take the following steps:
1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
2. Create a `Procfile` and inside of it place this line of code:
```
web: gunicorn pet_store_and_more.wsgi:application
```
3. `git add` and `git commit` the new requirements and Procfile and then git push the project to GitHub.
4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps/) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.
5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
6. Confirm the linking of the heroku app to the correct GitHub repository.
7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

Key | Value 
------------ | ------------- 
AWS_ACCESS_KEY_ID | `Your Value`
AWS_SECRET_ACCESS_KEY | `Your Value` 
DATABASE_URL | `Your Value` 
EMAIL_HOST_PASS | `Your Value` 
EMAIL_HOST_USER | `Your Value` 
SECRET_KEY | `Your Value` 
STRIPE_PUBLIC_KEY | `Your Value` 
STRIPE_SECRET_KEY | `Your Value` 
STRIPE_WH_SECRET | `Your Value`  
USE_AWS | `True` 
9. From the command line of your local IDE:
    + Enter the heroku postgres shell
    + Migrate the database models
    + Create your superuser account in your new database
Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).
10. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".
11. Once the build is complete, click the "View app" button provided and site should run as expected.

## Credits

### Content

### Media

### Acknowledgements
