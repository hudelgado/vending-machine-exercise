# The Vending Machine Exercise

This application implements a vending machine to be used as a web API.
It is implemented in Python 3 using Flask as a WSGI application and it uses Peewee as the ORM with an sqlite3 db.

The machine functionalities are:

- List the available products with their name and price.
- Buy products by inserting an amount of money.
- Return change if too much money is provided.
- Can be initially loaded with a set of products and coins.
- Both products and coins can be reloaded.
- Keeps track of the products and change that it contains.

## API
The machine API is divided into two api's, one for use by the customers to list and buy products, and a second one to be used by the service operators to list products and coins with their stocks and allow to reload the machine.

### Machine API `/api/machine`

#### `GET /api/machine/list` - Return the current machine products

Response: json
```json
[
  { "code": "1", "name": "Soda", "price": 10 },
  { "code": "2", "name": "Milk", "price": 45 }
]
```

#### `PUT /api/machine/buy` - Buy a product from the machine

Request body: json
```json
{
  "code": "1",
  "change": ["1p"]
}
```

### Service `/api/service`

#### `GET /api/service/get_products` - Return the current machine products

Response: json
```json
[
  { "code": "1", "name": "Soda", "quantity": 6, "price": 10 },
  { "code": "2", "name": "Milk", "quantity": 1, "price": 45 }
]
```


#### `PUT /api/service/load_products` - Recharge the machine with products

Request body: json
```json
[
  { "code": "1", "quantity": 6 },
  { "code": "new", "name": "new product", "price": 7, "quantity": 10 },
]
```
Response:
200 - True if success

#### `GET /api/service/get_coins` - Return the current machine coins

Response: json
```json
[
  { "denomination": "1p", "quantity": 10},
  { "denomination": "2p", "quantity": 3}
]
```

#### `PUT /api/service/load_coins` - Recharge the machine with coins

Request body: json
```json
[
  {"denomination": "1p", "quantity": 5},
  {"denomination": "2p", "quantity": 10}
]
```

Response:
200 - True if success


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

