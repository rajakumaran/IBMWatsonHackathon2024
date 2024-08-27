# IBMWatsonAIHackathon2024
<b>IBM Watson AI Hackathon 2024 August

Here is the link to my live demo of our AW Wingman app talking to IBM watsonx.ai LLMs and AI providing answers in multiple languages.</b>
This is 2nd and final part of our App's presentation.
*************************************************************************
https://youtu.be/Cmug1ib7fSQ
*************************************************************************
Installing Django
Here are the steps to install Django:

Step 1: Install Python
Make sure you have Python installed on your system. You can download the latest version from the official Python website if you haven't already.

Step 2: Install pip
pip is the package installer for Python. If you have Python installed, you should already have pip. You can check by running pip --version in your terminal.

Step 3: Install Django
Open your terminal and run the following command:
Bash
pip install django
This will install the latest version of Django.

Step 4: Install Django REST Framework
To build REST APIs, we'll use Django REST Framework. Install it by running:
Bash
pip install djangorestframework

Step 5: Create a new Django project
Create a new Django project by running:
Bash
django-admin startproject hotel_project
This will create a new directory called hotel_project with the basic structure for a Django project.

Step 6: Create a new Django app
Inside the hotel_project directory, create a new app called hotel:
Bash
python manage.py startapp hotel
This will create a new directory called hotel with the basic structure for a Django app.

Now that you have the models, serializers, and views, you can start building the application.
Here are the steps to build the application:
1. Create the database tables
Run the following command to create the database tables:
Bash
python manage.py makemigrations
python manage.py migrate
This will create the tables in your database based on the models you defined.

2. Create a superuser
Run the following command to create a superuser:
Bash
python manage.py createsuperuser
This will prompt you to enter a username, email, and password for the superuser.

3. Run the development server
Run the following command to start the development server:
Bash
python manage.py runserver
This will start the server and make your application available at http://localhost:8000/.

NOTE: after you successfully install and run the mentioned commands,  you should be able to nav to http://localhost:8000/api/v1/
and you can see the APIs for each table like this.

{
  "hotels": "http://localhost:8000/api/v1/hotels/",
  "bookings": "http://localhost:8000/api/v1/bookings/",
  "rooms": "http://localhost:8000/api/v1/rooms/",
  "room-availability": "http://localhost:8000/api/v1/room-availability/"
}
