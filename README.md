# Sample hello world program

This app uses Flask and Flask forms with a little Jinja to build a web app.

User will be prompted with a form requesting their name.

On submit, input data is validated and a new page is generated with a "Hello {name}" message written in HTML.

## Dependencies

Built in Python 3.8

Run the following command in a terminal to install dependencies:

`pip install -r requirements.txt
`

## Launch the app locally

Run main.py either through an IDE or via a terminal using:

`python main.py
`

Open a browser window, navigate to localhost:5000 or 127.0.0.1:5000



## Alternatively, build in Docker

`docker build -t hello_world .`

then:
`docker run -p  127.0.0.1:5000:5000 hello_world`

## Tests

Tests are written with the Behave framework.

Run either via an IDE, or cd into the tests directory via command line execute the following command:

`behave`