# Hotel-Management
 Python hotel management application with MySQL database includes 5 pages: Customer, Booking, Rooms, Service and Billing. It allows staff to efficiently manage guest 
 details, reservations, room allocation, additional services and billing.

# Main 
 1. Import the necessary modules:
    - `from tkinter import *`: Imports all Tkinter classes and functions for creating GUIs.
    - `from PIL import Image, ImageTk`: Imports the necessary classes from the Pillow library to manipulate images.
    - `from customer import Customer`: Imports the Customer class from the customer.py file.
    - `from room_booking import Booking`: Imports the Booking class from the room_booking.py file.
    - `from room import Room`: Imports the Room class from the room.py file.
    - `from service import Service`: Imports the Service class from the service.py file.
    - `from billing import Billing`: Imports the Billing class from the billing.py file.

 2. Definition of the `Hotel` class:
    - The `__init__` constructor initializes the main application window, defining its title, size and icon.
    - Creates multiple frames to organize UI elements.
    - Loads and displays images in certain frames.
    - Creates buttons for each functionality of the application (Customer, Booking, Rooms, Service, Billing).
    - Defines methods for opening dialog windows when a button is clicked.

 3. Definition of methods for each functionality:
    - `customer_window()`, `booking_window()`, `room_window()`, `service_window()`, `billing_window()`: These methods open a new window (Toplevel) for each 
 functionality by instantiating the corresponding classes (` Customer`, `Booking`, `Room`, `Service`, `Billing`).
  
