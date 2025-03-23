# Django Insurance Data Project

## Description
This project is a Django-based application for managing insurance data. It includes models for reporting entities, reporting plans, in-network files, and allowed amount files. The project also provides a REST API for accessing the data.

## Features
- **Reporting Entities**: Manage insurance reporting entities.
- **Reporting Plans**: Manage insurance plans associated with reporting entities.
- **In-Network Files**: Manage in-network files for each plan.
- **Allowed Amount Files**: Manage allowed amount files for each plan.
- **REST API**: Provides endpoints to access and manage the data.

## Installation
Follow these steps to set up the project locally.

### Prerequisites
- Python 3.8 or higher
- PostgreSQL

### Steps
1. Clone the repository:
   git clone https://github.com/Artur5Poghosyan/Insurance-data-analyze.git
   cd Insurance-data-analyze


2. Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  

3. Install dependencies:
    pip install -r requirements.txt

4. Set up the PostgreSQL database:
    Create a database named your_database_name.
    Update the DATABASES setting in settings.py with your PostgreSQL credentials:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Run migrations:
    python manage.py migrate

6. Load initial data
    python manage.py load_json_data

7. Create a superuser:
    python manage.py createsuperuser

8. Start the development server:
    python manage.py runserver

9. Access the application at:
    http://127.0.0.1:8000/


Usage
Accessing the Admin Interface
Go to http://127.0.0.1:8000/admin/.

Log in with your superuser credentials.

Using the REST API
The following API endpoints are available:

Reporting Entities: GET /api/reporting-entities/

Reporting Plans: GET /api/reporting-plans/

In-Network Files: GET /api/in-network-files/

Allowed Amount Files: GET /api/allowed-amount-files/

