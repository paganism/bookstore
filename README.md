# Book Store Site

This is a simple bookstore site.
It contains main page, book catalog with filters, book page, author page, cart and orders page.

Example you can see [here](http://80.211.16.55:5010)
# How to deploy on localhost
```bash
$ pip install -r requirements.txt
$ python3 manage.py runserver 5000

```
Then open the page [localhost:5000](http://localhost:5000) in browser.

## To run celery:
First of all install rabbit-mq (ubuntu example):
```
$ sudo apt install rabbitmq-server
```
Be shure that rabbitmq-server daemon is running
```
$ celery -A myshop worker -l info
$ celery -A myshop flower
```

# Project Goals

The code is written for educational purposes only.
