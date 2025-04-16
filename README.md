Little Lemon Restaurant Backend API

🔐 Authentication:
- POST /api/api-token-auth/
  - Description: Obtain an auth token by providing username and password.
  - Body: {"username": "your_username", "password": "your_password"}

📄 Menu Items:
- GET /api/menu-items/
  - Description: Retrieve all menu items.
- GET /api/menu-items/<id>/
  - Description: Retrieve a specific menu item.
- POST /api/menu-items/
  - Description: Create a new menu item (auth required).
- PUT /api/menu-items/<id>/
  - Description: Update a menu item (auth required).
- DELETE /api/menu-items/<id>/
  - Description: Delete a menu item (auth required).

📅 Table Booking:
- GET /api/tables/
  - Description: Retrieve all bookings.
- GET /api/tables/<id>/
  - Description: Retrieve a specific booking.
- POST /api/tables/
  - Description: Create a new table booking.
- PUT /api/tables/<id>/
  - Description: Update a booking.
- DELETE /api/tables/<id>/
  - Description: Delete a booking.

To run all tests:
$ python manage.py test

Tests included:
- Menu model test (`test_models.py`)
- Menu view test (`test_views.py`)


