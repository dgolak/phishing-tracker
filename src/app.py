# -*- coding: utf-8 -*-
"""app.py."""

from database import init_db

from flask import Flask

from page import Page


app = Flask(__name__)
app.config['DEBUG'] = True

init_db()
page = Page(app)
if __name__ == '__main__':
    app.run()
