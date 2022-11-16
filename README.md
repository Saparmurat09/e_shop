# E-Shop

This is an API for e-shop which allow to manage products, comment and rate items. You can also add items to cart and make an order.


### Documentation

Documentation for Courses API was made apiary.io

https://eshop36.docs.apiary.io

Find documentation in the above link

### Prerequisites
---
- git client https://git-scm.com/downloads
- Python version 3.10 https://www.python.org/downloads/
- IDE VS Code https://code.visualstudio.com (optional)

### Installing
---

Execute following CLI commands on your machine


```
$ git clone https://github.com/Saparmurat09/e_shop.git

$ cd e_shop

# setup virtual environment inside project folder
$ python -m venv env

# activate virtual environment
$ source /venv/bin/activate

#install all dependencies

$(venv) pip install -r requirements.txt 
```

Before running project you have to set environment variables in .env file

```
$ touch .env
```

specify following variables inside .env file:

```
SECRET_KEY = '{your secret key for project}'

# use False in deployment
DEBUG = True

# it's necessary to add database detail in deployment

```

## Running the tests

Tests will be located in shopapp/test folder

```
$ python3 manage.py test
```

## Deployment

currently there are no deployment details

they will be added soon

## Authors

* [github.com/Saparmurat09](https://github.com/Saparmurat09/courses)
