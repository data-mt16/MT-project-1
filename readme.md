# Django Car Dealership API & Dashboard

This is a full-stack web application built with Django and Django REST Framework. It manages data for a car dealership, including customers, products, shippers, and orders, and provides a complete REST API for all models. It also features a user authentication system and a business intelligence dashboard for running complex queries.

---

## Features

- **User Authentication**: Full user registration, login, and logout system.
- **Complete REST API**: Full CRUD (Create, Read, Update, Delete) API endpoints for all database models, built with DRF's ViewSets and Routers.
- **Business Intelligence Dashboard**: A protected dashboard for logged-in users to run 10 different complex analytical queries on the database.
- **Dynamic Frontend**: The dashboard uses JavaScript (`fetch` API) to interact with the backend API and display results without page reloads.
- **Bootstrap UI**: A clean and simple frontend styled with Bootstrap.

---

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML, Bootstrap 5, JavaScript
- **API Testing**: Postman

---

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/data-mt16/MT-project-1.git](https://github.com/data-mt16/MT-project-1.git)
    cd MT-project-1
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the PostgreSQL Database:**

    - Make sure PostgreSQL is installed and running.
    - Create a new database (e.g., `car_dealership_db`).

5.  **Configure Environment Variables:**

    - Create a `.env` file in the project root.
    - Add the following variables, replacing the placeholder values:
      ```env
      SECRET_KEY='your-django-secret-key'
      DATABASE_PASSWORD='your-postgres-password'
      ```

6.  **Run Database Migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser** to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

8.  **(Optional) Load Initial Data:**

    - The project contains SQL scripts with sample data. Use a tool like DBeaver to connect to your database and run the `INSERT` scripts for `customer_t`, `product_t`, `shipper_t`, and `order_t`.

9.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## API Usage

The API is browsable. Once the server is running, you can explore the main API root at `http://127.0.0.1:8000/api/`.

### Main Endpoints

- **CRUD Operations**:
  - `/api/products/`
  - `/api/customers/`
  - `/api/shippers/`
  - `/api/orders/`
- **Business Intelligence Reports**:
  - `/api/reports/customer-distribution/`
  - `/api/reports/top-vehicle-makers/`

A Postman collection with documented requests can also be provided.
