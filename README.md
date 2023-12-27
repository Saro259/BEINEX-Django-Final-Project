# Django Ecommerce API
* Registration using Email
  * Allows users to register using email.
  * Can set expiration time and length on generated tokens for account verification.
* Basic E-commerce features.
* Deployed for local development and production.
# Technologies Used
* Django Rest Framework
* SQLlite
# ER Diagram
* The Entity-Relationship Diagram is given as follows: https://dbdiagram.io/d/656cc15d56d8064ca049ef17
![image](https://github.com/Saro259/BEINEX-Django-Final-Project/assets/73172999/4713104e-9503-49e8-b148-5e443674957a)

# Quick Start
* Clone this repository to your local machine. Start the project manually using a virtual environment.
1. Create a Python virtual environment and activate it.
2. Open up your terminal and run the following command to install the packages used in this project.
  ``` 
   $ pip install -r requirements.txt
  ```  
3. Set up a SQLlite database for the project in your desired universal database management tool.
4. Run the following commands to setup the database tables and create a superuser.
   ```
   $ python manage.py migrate
   $ python manage.py createsuperuser
   
   ```
5. Run the development server using:
   ```
   $ python manage.py runserver
   ```
6. Open a browser and go to http://localhost:8000/
