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
[wireframes](https://github.com/vladimir-cmd/vacation-planner-web-app/tree/master/wireframes-mockups) in: 
[Front Page Before Login](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Front_Page_Before_Login.png), 
[Front Page After Login](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Front_Page_After_Login.png), 
[User Profile Page](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Users_profile.png), 
[Add New Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Add_New_Entry.png), 
[Edit Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Edit_Entry.png), 
[Manage Entry](https://github.com/vladimir-cmd/vacation-planner-web-app/blob/master/wireframes-mockups/Manage_Entries.png)

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

- [HTML](https://en.wikipedia.org/wiki/HTML)

  - Semantic markup language as the shell of the site.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - Programming language for the workability of the site.

- [FontAwesome](https://fontawesome.com/)

  - **FontAwesome** provided the icons used on the page.

- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
  
- [Python Django](https://www.djangoproject.com/)

  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- [Visual Studio Code](https://code.visualstudio.com/)

  - IDE (Integrated Development Environment).

- [IntelliJ Idea Community Edition](https://www.jetbrains.com/idea/)

  - IDE (Integrated Development Environment).

- [GitHub](github.com/)

  - The remote hosting platform.

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - To see visually the elements of what each code produced, what happens if code is changed, and responsiveness of different device sizes.

- [Jigsaw](https://jigsaw.w3.org/css-validator)

  - To check for any errors in the CSS code.

## Testing

Testing information is found on a separate file [TESTING.MD](https://github.com/vladimir-cmd/pet_store_and_more/TESTING.md)

## Deployment

Creation of website

This website is deployed using Heroku.

## Credits

### Content

### Media

### Acknowledgements
