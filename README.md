# Auctions

## Overview
This project is an e-commerce auctions site that allows users to register an account, log in, view current auction listings, post auction listings, place bids on current listings, comment on those listings, add listings to their “watchlist”. It also provides users with an ability to filter items by their categories and an admin interface to manage the application.

## Features
1. Register an account
2. Log in
3. View current auction listings
4. Post auction listings
5. Place bids on current listings
6. Comment on those listings
7. Add listings to their “watchlist”
8. Filter the item by using the category
9. Use Admin Interface to manage the Application.

## Technologies Used
- Python
- Django
- JavaScript
- HTML
- CSS
- Bootstrap
- SQLite
- ORM

## Requirements
You only need to have Django installed. You can install it using pip:

## Code Structure
The project contains the following important files:

1. `models.py`: This file contains the database models used in the project. We have five models:
   - `User`: Represents a user in the system.
   - `Category`: Represents a category that a listing belongs to.
   - `Listings`: Represents a listing in the auction site.
   - `Bids`: Represents a bid placed by a user on a listing.
   - `Comments`: Represents a comment made by a user on a listing.

2. `admin.py`: This file is used to customize the Django admin site. It includes `UserAdmin`, `CategoryAdmin`, `ListingsAdmin`, `BidsAdmin`, and `CommentsAdmin` for managing the corresponding models.

3. `urls.py`: This file contains all the URL mappings for the application.

4. `views.py`: This file contains all the views for the application. Each view is a function that takes a Web request and returns a Web response.

For more details on the code, please refer to the comments in each file.

## Running the application
1. Clone this repository.
2. Navigate to the project directory.
3. Run the following command to start the Django server:
   + python manage.py runserver
4. Access the application at `localhost:8000` in your web browser.
