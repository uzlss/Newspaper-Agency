![favicon](static/favicon.ico)

# Newspaper-Agency
Newspaper-Agency is a web application designed to manage digital newspapers. It provides a platform for newspaper agencies to manage their content and redactors efficiently.

## Check it out!
[Newspaper-Agency deployed to Render](https://newspaper-agency-cl9y.onrender.com/)
###### Test credentials:
###### login: test.user
###### password: _t3ST#US3r

## Features
- Soft UI design
- Manage newspaper articles
- Manage redactor profiles
- User authentication and authorization

## Home page
![Home_page](index.png)

## Installation
1. **Clone the repository**
```shell
   git clone https://github.com/uzlss/Newspaper-Agency.git
   cd Newspaper-Agency
```
2. **Create a virtual environment and install requirements**
> If you are using PyCharm - it may propose you to automatically create venv for your project 
    and install requirements in it, but if not:
```shell
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
```
3.**Run migrations**
```shell
python manage.py migrate
```
4.**(Optional) Load fixture**
> Note: All users' passwords will not work, so you may need to create superuser using ```python manage.py createsuperuser``` or modify users via ORM.
```shell
python manage.py loaddata Newsdesk/fixtures/data.json
```

5.**Run the server**
> If you are using PyCharm, it may automatically configure the Run option (Shift+F10 by default). If not, run:

```shell
python manage.py runserver
```

### Database structure
![db_structure](https://github.com/user-attachments/assets/8607f608-ad2f-42d7-a5ee-1f35c4160bad)
