# The Vending Machine Exercise


## Requirements
This application uses Python3 and it is recomended to use a virtual environment for the project packages.

- See requirements.txt

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

## Development

Define the environment variables:
```
$ export FLASK_APP=vending_machine
$ export FLASK_ENV=development
```

Initialize the database:
```
$ flask init-db
```

Optionally load the initial sample data with products and change:
```
$ flask load-sample
```

Launch a development server:
```
$ flask run
```

## Run


## Test
