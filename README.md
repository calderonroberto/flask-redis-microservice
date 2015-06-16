# An example microservice using Flask and Redis.

This microservice uses Flask and Redis to store keys.

Try it:

```
curl -H "Content-Type: application/json" -X PUT -d '{"value":123}' https://flask-redis.herokuapp.com/mysensor

curl https://flask-redis.herokuapp.com/mysensor
```

And another instance (by [https://github.com/itamarhaber/flask-redis-microservice](itarmarhaber)):
[https://github.com/itamarhaber/flask-redis-microservice](https://github.com/itamarhaber/flask-redis-microservice)

```
curl -H "Content-Type: application/json" -X PUT -d '{"value":123}' https://flask-redis-microservice.herokuapp.com/mysensor

curl https://flask-redis-microservice.herokuapp.com/mysensor
```

## Dependencies:

* Python >2.7
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

[https://github.com/itamarhaber](itarmarhaber)
