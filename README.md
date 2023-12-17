# Django Project

- [Setup Project](#Setup-Project)
- [Create Template](#Create-Template)
- [Create Login Authentication](#Create-Authentication-Login)
- [Create Logout Authentication](#Create-Authentication-Logout)

## Setup-Project

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
5. Download the MySQL COmmunity at `https://dev.mysql.com/downloads/`
6. Create a `requirements.txt` for the other to set up your project
   ```
     pip freeze > requirements.txt
   ```
   - to install the dependencies by other next time
   ```
     pip install -r requirements.txt
   ```
7. Setup version control with git
   ```git
      git config --global user.name "potatoscript"
      git config --global user.email "potatoscript@yahoo.com"
      git config --global push.default matching
      git config --global alias.co checkout
      git init
      git add .
      git commit -am "Initial commit"
   ```
8. Push to github `first create a new repository in your github account with a name like Django-CRM`
   ```git
      git remote add origin https://github.com/potatoscript/Django-CRM.git
      git branch -M main
      git push -u origin main
   ```
9. Create Project

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

## Create-Template

1. Create a `templates` folder under applicationName directory
2. Create `navbar.html` under the template
   ```html
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
     <div class="container-fluid">
       <a class="navbar-brand" href="{% url 'home' %}">Django CRM</a>
       <button
         class="navbar-toggler"
         type="button"
         data-bs-toggle="collapse"
         data-bs-target="#navbarSupportedContent"
         aria-controls="navbarSupportedContent"
         aria-expanded="false"
         aria-label="Toggle navigation"
       >
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="navbarSupportedContent">
         <ul class="navbar-nav me-auto mb-2 mb-lg-0">
           <li class="nav-item">
             <a class="nav-link" href="#">Link</a>
           </li>
         </ul>
       </div>
     </div>
   </nav>
   ```
3. Create `base.html` under the template to share with all the pages (get the sample code from https://getbootstrap.com/Introduction)<br>
   and include the `navbar.html`
   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <title>Bootstrap demo</title>
       <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
         rel="stylesheet"
         integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
         crossorigin="anonymous"
       />
     </head>
     <body>
       {% include 'navbar.html' %}
       <div class="container">
         <br />
         <h1>Hello, world!</h1>
       </div>
       <script
         src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
         integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
         crossorigin="anonymous"
       ></script>
     </body>
   </html>
   ```
4. Create `home.html` under the template and include the `base.html` into it

   ```html
   {% extends 'base.html' %}/ {% block content %}
   <h1>Hello World</h1>
   {% endblock %}
   ```

## Create-Authentication-Login

1. setting `views.py`

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth import authenticate, login, logout
   from django.contrib import messages

   def home(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               messages.success(request, "You Have Been Logged In")
           else:
               messages.success(request,"There was an error logging in, Please try again...")
           return redirect('home')
       return render(request, 'home.html', {})

   def logout_user(request):
       pass
   ```

2. setting `home.html`

   ```html
   {% extends 'base.html' %}/ {% block content %}
   <div class="col-md-6 offset-md-3">
     {% if user.is_authenticated %}
     <h1>Hello World</h1>
     {% else %}
     <h1>Login</h1>
     <br />
     <form method="POST" action="{% url 'home' %}">
       {% csrf_token %}
       <div class="mb-3">
         <input
           type="text"
           class="form-control"
           name="username"
           placeholder="username"
           required
         />
       </div>
       <br />
       <div class="mb-3">
         <input
           type="password"
           class="form-control"
           name="password"
           placeholder="password"
           required
         />
       </div>
       <button type="submit" class="btn btn-secondary">Login</button>
     </form>
   </div>
   {% endif %} {% endblock %}
   ```

   ##### {% csrf_token %} is for security issue to prevent the hacking from the

3. setting `base.html`
   ```html
     <div class="container"><br>
        <br/>
        {% if messages %}
          {% for message in messages %}
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
              <strong>{{message}}
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
          {% endfor %}
        {% endif %}
        {% block content %}
        {% endblock%}
      </div>
   ```

## Create-Authentication-Logout

1. setup application `urls.py`

```python
   urlpatterns = [
      ...,
      path('logout/', views.logout_user, name='logout'),
   ]
```

2. setup `views.py`

```python
  def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')
```

3.  add a link in the navbar

```html
<!--we only want the logout link to be appear when the user was logged out-->
<ul class="navbar-nav me-auto mb-2 mb-lg-0">
  {% if user.is_authenticated %}
  <li class="nav-item">
    <a class="nav-link" href="{% url 'logout' %}">Logout</a>
  </li>
  {% else %}
  <li class="nav-item">
    <a class="nav-link" href="{% url 'home' %}">Login</a>
  </li>
  {% endif %}
</ul>
```
