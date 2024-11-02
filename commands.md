# Commands Log

## Project Setup

### Create Django Project
- **Command:** `django-admin startproject studyhub`
- **Purpose:** Initializes a new Django project named `studyhub`.
- **Context:** Run this command in the terminal after navigating to the desired project directory.
- **Notes:** Ensure Django is installed (`pip install Django`) before running this command.


## Running the Development Server

### Start Django Development Server
- **Command:** `python manage.py runserver`
- **Purpose:** Starts the Django development server to test the application locally.
- **Context:** Run this command from the root directory of the Django project (e.g., `studyhub`).
- **Notes:** 
  - Default server runs on `http://127.0.0.1:8000`.
  - Use `python manage.py runserver <port_number>` to specify a different port (e.g., `python manage.py runserver 8080`).


## Creating a Django App

### Start New Django App
- **Command:** `python manage.py startapp base`
- **Purpose:** Creates a new Django app named `base`, where you can add models, views, templates, and other app-specific files.
- **Context:** Run this command from the root directory of the Django project (e.g., `studyhub`).
- **Notes:** 
  - After creating the app, remember to add `'base'` to the `INSTALLED_APPS` list in `settings.py` to activate it.
  - The `base` app might serve as the main or foundational app for general functionality.

