# Book Store Site

This is a bookstore site. It contains main page, catalog with filters, book page, author page and also it has bin page (in development)

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

The code is written for educational purposes.
