# The Vending Machine Exercise


## Requirements
This application uses Python 3 and it is recomended to use a virtual environment for the project packages.

- Flask
- Peewee
- pytest
- coverage

## Install
Create a virtual environment and use it:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

Or on Windows cmd:
```
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

Install the required packages:
```
$ pip install -r requirements.txt
```

Define the environment variables:
```
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
```
$ flask init-db
```

Optionally load the initial sample data with products and coins:
```
$ flask load-sample
```

## Run

Launch a built-in Flask development server:
```
$ flask run
```
After launch the server will be on localhost at the default port 5000.

The run command can receive the host and port addresses to which it should bind to:
```
$ flask run -h 0.0.0.0 -p 8080
```
That will make the server available on localhost at port 8080 to any host in the local network and 

## Test
Start the tests with:
```
$ pytest
```

Run tests with coverage report:
```
$ coverage run -m pytest
$ coverage report
$ coverage html  # open htmlcov/index.html in a browser
```