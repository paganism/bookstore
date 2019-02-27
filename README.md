# Book Store Site

This is a simple bookstore site.
It contains main page, book catalog with filters, book page, author page, cart and orders page.

# How to deploy on localhost
```bash
$ pip install -r requirements.txt
```
Then open the page [localhost:5000](http://localhost:5000) in browser.

## To run celery:
```
$ celery -A myshop worker -l info
$ celery -A myshop flower
```

# Project Goals

The code is written for educational purposes only.
