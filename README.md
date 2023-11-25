# PG4You - Your Ultimate PG Accommodation Solution!

Are you relocating to a new city and need a comfortable and convenient PG accommodation? Look no further! PG4You is here to simplify your search and help you find the perfect PG that suits your preferences and needs.

## What Is PG4You?

PG4You is an innovative platform designed to connect PG owners with individuals seeking accommodations in new cities. Our user-friendly website offers a wide range of PG options, making your relocation process stress-free and enjoyable.

## Key Features of PG4You

- Comprehensive PG Listings
- Personalized Search
- Verified Listings
- Seamless Communication
- Reviews and Ratings
- Safety First

## About This Video

In this demo video, we walk you through the various features and benefits of PG4You. See how easy it is to find and book your dream PG accommodation using our platform. [Watch the Demo Video](https://youtu.be/fngMVOJ-mBQ?si=ehY6ji1zNzHF7Sr3)

## Connect with PG4You

- Email: [ayushibanas1307@gmail.com]

# PG4You Project

PG4You is a web application developed using HTML, CSS, and JavaScript for the frontend and Python with the Django framework for the backend. PostgreSQL, powered by pgAdmin, is used for database connectivity.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed (prefer 3.8.9)
- [Django](https://www.djangoproject.com/) framework installed (prefer 3.2)
- [PostgreSQL](https://www.postgresql.org/) and [pgAdmin](https://www.pgadmin.org/) installed and configured (prefer 14)

### Installation

1. **Clone the repository and navigate to the project directory:**

    ```bash
    git clone https://github.com/shi-hash13/Demo-project1.git
    cd pgproj
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Database Configuration:**

    Open pgAdmin and create a new database. Update the `DATABASES` configuration in `settings.py` with your PostgreSQL credentials.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'pgdb25112023',
            'USER':'postgres',
            'PASSWORD': 'Your pgAdmin password',
            'HOST':'localhost',
            'PORT':'5432',
        }
    }
    ```

    Make sure to restore the database in pgAdmin.

4. **Application definition:**

    In `settings.py`, add `pgapp` to `INSTALLED_APPS`.

    ```python
    INSTALLED_APPS = [
        'pgapp',
    ]
    ```

5. **Apply Migrations for Database Connectivity:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

For support or inquiries, contact [ayushibanas1307@gmail.com].


