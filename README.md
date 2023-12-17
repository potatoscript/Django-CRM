# Django Project
## Step by step
1. Create project directory 
   - `mkdir /c/projectName` 
   - `cd /c/projectName`
2. Create virtual environment 
   - `python -m venv virtualName`
3. Turn on your virtual Environment
   - `source virtualName/Scripts/activate`  
4. Install the necessary libraries
   ```
     pip install django
   ```
   ```
     pip install mysql
   ```
   ```
     pip install mysql-connector
   ```
   ```
     pip install mysql-connector-python
   ```
6. Download the MySQL COmmunity at `https://dev.mysql.com/downloads/`
7. Create a `requirements.txt` for the other to set up your project
   ```
     pip freeze > requirements.txt
   ```
   - to install the dependencies by other next time
   ```
     pip install -r requirements.txt
   ``` 
8. Setup version control with git
   ```git
      git config --global user.name "potatoscript"
      git config --global user.email "potatoscript@yahoo.com"
      git config --global push.default matching
      git config --global alias.co checkout
      git init
      git add .
      git commit -am "Initial commit"
     ```
9. Push to github `first create a new repository in your github account with a name like Django-CRM`
   ```git
      git remote add origin https://github.com/potatoscript/Django-CRM.git
      git branch -M main
      git push -u origin main
   ```
10. Create Project
   ```bash
     django-admin startproject projectName
     cd projectName/
   ```
11. Create Application
    ```
     python manage.py startapp applicationName
    ```
12. Add the application into `INSTALLED_APPS` in setting.py
    ```python
      INSTALLED_APPS = [
         ...
         'applicationName'
      ]
    ```
13. Setting the Database in setting.py
    ```python
      DATABASES = {
        'default' : {
           'ENGINE' : 'django.db.backends.mysql',
           'NAME' : 'databaseName',
           'USER' : 'root',
           'PASSWORD' : '#password',
           'HOST' : 'localhost',
           'PORT' : '3306'
         }
     }
    ```
14. Create `mydb.py` at the location same as manage.py to test your database connection
    ```python
    import mysql.connector

    database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root'
    )
    
    # prepare a cursor object
    currorObject = database.cursor()
    
    # Create a database
    currorObject.execute("CREATE DATABASE office")
    
    print("All Done!")
    ```
15. Migrate or create your database in the MySQL server
    ```bash
     python manage.py migrate
    ```
16. Create super user
    ```bash
     winpty python manage.py createsuperuser
     username : admin
     password :
     ...
    ```
17. Include the application urls into project's urls.py
    ```python
     from django.urls import path, include
     urlpatterns = [
       ...,
       path('', include('applicationName.urls')),
     ]
    ```
18. Create urls.py in applicationName
    ```python
     from django.urls import path
     from . import views
     urlpatterns = [
       path('', views.home, name='home'),
     ]
    ```
19. Editing the `views.py`
    ```python
     from django.shortcuts import render

     def home(request):
       return render(request, 'home.html', {}) 
    ```
20. Create a templates folder under applicationName directory
     
