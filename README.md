# Flask Redis SQLAlchemy - Error Demonstration

## Installing dependencies with pip

pip install --require-hashes -r requirements.txt

## Create database

flask create_database

## Running

### Start redis at port 7000
redis-server --port 7000

### Run worker.<i></i>py
python worker.<i></i>py

### Stark flask app
flask run

## Testing

Go to the browser and type http:<i></i>//127.<i></i>0.0.1:5000/send_email

