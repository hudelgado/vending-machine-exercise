# The Vending Machine Exercise

This application implements a vending machine as an API.
It is implemented in Python 3 using Flask as a WSGI application and Peewee as the ORM with sqlite3.

The machine functionalities are:

- Buy products by inserting an amount of money.
- Return change if too much money is provided.
- Can be initially loaded with a set of products and coins.
- Both products and coins can be reloaded.
- Keeps track of the products and change that it contains.

## API
The API contains two endpoints. A machine module to perform the sales, and a service module to recharge the machine.

### Machine API `/api/machine`

#### `PUT /api/machine/buy` - Buy a product from the machine

Json body:
```json
{
  "code": "1",
  "change": ["1p"]
}
```

### Service `/api/service`

#### `PUT /api/service/load_products` - Recharge the machine with products

Json body:
```json
[
  { "code": "1", "quantity": 6 },
  { "code": "2", "quantity": 10 },
]
```

#### `PUT /api/service/load_coins` - Recharge the machine with coins

Json body:
```json
["1p", "1p", "2p"]
```

## Install

### Requirements
In order to run it is necessary to have Python 3.
It is recomended to use a virtual environment to manage the packages used in the application.

Create a virtual environment and use it:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Or on Windows cmd:
```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

Install the required packages:
```bash
$ pip install -r requirements.txt
```

Define the environment variables:
```bash
$ export FLASK_APP=vending_machine
$ export FLASK_ENV=development
```

Or on Windows cmd:
```
set FLASK_APP=vending_machine
set FLASK_ENV=development
flask run
```

Initialize the database:
```bash
$ flask init-db
```

Optionally load the initial sample data with products and coins:
```bash
$ flask load-sample
```

## Run

Launch a built-in Flask development server:
```bash
$ flask run
```
After launch the server will be on localhost at the default port 5000.

The run command can receive the host and port addresses to which it should bind to:
```bash
$ flask run -h 0.0.0.0 -p 8080
```
That will make the server available on localhost at port 8080 to any host in the local network.

> The Flask's built-in server is not suitable for production, refer to the [documentation](https://flask.palletsprojects.com/en/1.1.x/deploying/) for further info.

## Test
Start the tests with:
```bash
$ pytest
```

Run tests with coverage report:
```bash
$ coverage run -m pytest
$ coverage report
$ coverage html  # open htmlcov/index.html in a browser
```

