# To Do

## Introduction

We are going to use the [Flask](http://flask.pocoo.org/) framework to create a simple To Do list
application in Python. The view templates will be defined using [Jinja 2](http://jinja.pocoo.org/docs/dev/templates/)
and the users and todo items will be stored in a [MongoDB](https://www.mongodb.org/) database hosted
on [Compose](http://www.compose.io).

## Install Python

You will need to install the [Python](https://www.python.org/downloads/) download and execute the installer;

Setting up their Windows paths:
```
Python path C:/FOLDER/PYTHON
Pip path C:/FOLDER/PYTHON/Scripts
```



## Install Flask

You will need to install the [Flask](http://flask.pocoo.org/) framework by executing the following command:

```
pip install flask
```

## Steps 1 & 2

The todo1 project implements the login functionality using cookies. The login is very basic and
only checks that the password is the same as the username.

The todo2 project implements the login functionality using a session. The login still only checks
that the password is the same as the username.

## Install MongoEngine

We are going to use MongoDB to store out users and to do list items. We need the 
[Flask MongoEngine](https://flask-mongoengine.readthedocs.org/en/latest/) which can be 
installed by executing the following command:

```
pip install flask-mongoengine
```

## Step 3

The todo3 project checks is checking the username and password against entries in the MongoDB
database.

## Step 4

The todo4 project is retrieving, adding and deleting the to do list items in the database.
