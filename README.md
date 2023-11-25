🏠 Welcome to PG4You - Your Ultimate PG Accommodation Solution! 🏠

Are you relocating to a new city and need a comfortable and convenient PG accommodation? Look no further! PG4You is here to simplify your search and help you find the perfect PG that suits your preferences and needs.

🔍 What Is PG4You? 🔍
PG4You is an innovative platform designed to connect PG owners with individuals seeking accommodations in new cities. Our user-friendly website offers a wide range of PG options, making your relocation process stress-free and enjoyable.

🌟 Key Features of PG4You 🌟
✅ Comprehensive PG Listings: Find the ideal PG accommodation with detailed descriptions and amenities.
✅ Personalized Search: Filter results based on your preferences - location, budget, and more.
✅ Verified Listings: Trustworthy and accurate information to make informed decisions.
✅ Seamless Communication: Connect directly with PG owners to get all your queries answered.
✅ Reviews and Ratings: Learn from others' experiences and make confident choices.
✅ Safety First: Prioritize security and privacy through our secure platform.

🎥 About This Video 🎥
In this demo video, we walk you through the various features and benefits of PG4You. See how easy it is to find and book your dream PG accommodation using our platform.
https://youtu.be/fngMVOJ-mBQ?si=ehY6ji1zNzHF7Sr3

🌐 Connect with PG4You 🌐
📧 Email: [ayushibanas1307@gmail.com]

# PG4You Project

PG4You is a web application developed using HTML, CSS, and JavaScript for the frontend and Python with the Django framework for the backend. PostgreSQL, powered by pgAdmin, is used for database connectivity.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed prefer 3.8.9
- [Django](https://www.djangoproject.com/) framework installed prefer 3.2
- [PostgreSQL](https://www.postgresql.org/) and [pgAdmin](https://www.pgadmin.org/) installed and configured prefer 14

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pg4you.git
   cd pg

   Install Python dependencies:
    pip install -r requirements.txt

   Database Configuration
    
In your README file, you can mention the requirement file and how to install the dependencies using it. Here's an example of how you can include this information:

markdown
Copy code
# PG4You Project

PG4You is a web application developed using HTML, CSS, and JavaScript for the frontend and Python with the Django framework for the backend. PostgreSQL, powered by pgAdmin, is used for database connectivity.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [Django](https://www.djangoproject.com/) framework installed
- [PostgreSQL](https://www.postgresql.org/) and [pgAdmin](https://www.pgadmin.org/) installed and configured

### Set an environment

Run the following to create your environment



### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pg4you.git
   cd pgproj
# Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
The list of dependencies and their versions are specified in the requirements.txt file.



# Database Configuration

Open pgAdmin and create a new database.
Update the DATABASES configuration in settings.py with your PostgreSQL credentials.

DATABASES = {
   
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pgdb25112023',
        'USER':'postgres',
        'PASSWORD': 'Your pg'Admin password,
        'HOST':'localhost',
        'PORT':'5432',
    }

}

Make sure to restore database in pgAdmin 

# Application definition
In setting.py add pgapp in INSTALLED_APPS

INSTALLED_APPS = [

    'pgapp'
]

# Apply Migrations for Database Connectivity

bash
Copy code
python manage.py makemigrations
python manage.py migrate 


# Run the development server:

bash
Copy code
python manage.py runserver
Requirements







    
   
   

