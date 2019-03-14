![Sigma-Alfa](https://cdn1.iconfinder.com/data/icons/dicticons-text-alignment/32/sigma-128.png)
# Sigma 

Django application for scheduling, monitoring and grading classes. 

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install:
1. Python 3
2. Django 2.1.7
3. PostgreSQL

[Install PostgreSQL - In case it is not installed in the system](https://github.com/pedrogritter/sigma/wiki/Install-PostgreSQL)

### Installing 
Here is a step by step series of examples that tell you how to get a development env running

+  Create or go to the desired folder destination

+  Create a virtual environment:

```
virtualenv venv
```

________________________________________________________________________

+  **__In case you use Python 2.7__**

   Change the version of Python for the virtual environemnt with this command:
   
```
virtualenv --python=/usr/bin/python3.6 venv
```
_________________________________________________________________________
+ Activate the environment:

```
. venv/bin/activate
```

If it worked, terminal prompt should be similar to this:

```
(venv) User@computer-UX430UAR:~/Documents/repository$
```

+  Clone the repository to the destination folder

```
git clone https://github.com/pedrogritter/sigma.git
```
+ Install required dependencies by running:

```
# Note on Python 3 :you need to install python3-dev using the following command :

sudo apt-get install python3-dev # debian / Ubuntu


# Install pip3 for python3:

sudo apt install python3-pip

# Then install all the packages in requirements.txt

pip3 install -r requirements.txt

```


____________________________________________________________________________________________

#### Django Database Connection

The master branch is the production version there for the database settings are configured for Heroku Postgres DB.
The connection settings need to be changed to access a local postgres database.
____________________________________________________________________________________________________________________________
+ First, create a database for our Django project. Enter __psql__ prompt :

```
psql
```
+ Create database:

```
psql (10.6 (Ubuntu 10.6-0ubuntu0.18.04.1))
Type "help" for help.

user=# CREATE DATABASE project_db;
```
__Remember to end all commands at an SQL prompt with a semicolon.__

+ Next, we will create a database user which we will use to connect to and interact with the database. Set the password to something strong and secure:

```
psql (10.6 (Ubuntu 10.6-0ubuntu0.18.04.1))
Type "help" for help.

user=# CREATE USER project_admin WITH PASSWORD 'password';
```
Afterwards, we'll modify a few of the connection parameters for the user we just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to "read committed", which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django project will be set to use GMT:

+ In __psql__:
```
ALTER ROLE project_admin SET client_encoding TO 'utf8';
ALTER ROLE project_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE project_admin SET timezone TO 'GMT';
```

+ Now, all we need to do is give our database user access rights to the database we created:

```
GRANT ALL PRIVILEGES ON DATABASE project_db TO project_admin;
```

+ Exit the SQL prompt to get back to the user's shell session:

```
\q
```
________________________________________________________________________________________________

+ Next, modifiy the  **settings.py** to connect to a local DB:

```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'project_db',
#         'USER': 'project_admin',
#         'PASSWORD': 'lti2019',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

```
+ Change to this:
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#DATABASE_URL = os.environ['DATABASE_URL']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'project_db',
         'USER': 'project_admin',
         'PASSWORD': 'password',
         'HOST': 'localhost',
         'PORT': '',
     }
 }
```

+ Lastly, comment this line at the end o __setting.py__ too:

```
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

```


### Deployment
This project is deployed on [Heroku](https://www.heroku.com/) over [here](http://sigma-alfa.herokuapp.com/)

To deploy this on a live system enter the following command:

```
python3 manage.py runserver
```

**A development server should be running at http://127.0.0.1:8000/**


**Remember that all development should be done in a dev branch before being merged with the master branch for production**


## Built With

[Django 2.1.7](https://www.djangoproject.com/)- Python Web framework used

[Vue.js 2.2](https://vuejs.org/) - Progressive Javascript framework

[Bulma](https://bulma.io)- Modern CSS Framework

[PostgreSQL](https://www.postgresql.org/)

[Django Packages](https://djangopackages.org/)- A directory of reusable apps, sites, tools, and more for your Django projects.
