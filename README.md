[![Build Status](https://travis-ci.org/calderonroberto/flask-redis-microservice.svg?branch=master)](https://travis-ci.org/calderonroberto/flask-redis-microservice)

[![Code Climate](https://codeclimate.com/github/calderonroberto/flask-redis-microservice/badges/gpa.svg)](https://codeclimate.com/github/calderonroberto/flask-redis-microservice)

# An example microservice using Flask and Redis.

This microservice uses Flask and Redis to store keys.

## Deploy your own:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Try it:

```
curl -H "Content-Type: application/json" -X PUT -d '{"value":123}' https://flask-redis.herokuapp.com/mysensor

curl https://flask-redis.herokuapp.com/mysensor
```

And another instance (by [itamarhaber](https://github.com/itamarhaber)
):

[https://github.com/itamarhaber/flask-redis-microservice](https://github.com/itamarhaber/flask-redis-microservice)

```
curl -H "Content-Type: application/json" -X PUT -d '{"value":123}' https://flask-redis-microservice.herokuapp.com/mysensor

curl https://flask-redis-microservice.herokuapp.com/mysensor
```

## Dependencies:

* Python >2.7 (Sorry boys not Python3 compatible)
* Flask
* Redis

To install dependencies run:

```
pip install flask
pip install redis
```

To run the tests run:

```
python app_tests.py
```

To run the application:

```
python app.py
```

## Other Contributors:

[itamarhaber](https://github.com/itamarhaber)
