# -*- coding: utf-8 -*-
"""import.py."""
from classes.Ip import Ip
from classes.Country import Country
from classes.Brand import Brand
from classes.Hoster import Hoster
from database import init_db

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

init_db()

"""
ip = Ip()
i = ip.add("1.1.1.3")
if i:
    print("+ New Ip added")
else:
    print("- Couldn't add Ip")
"""

country = Country()
co = country.add("Temporary")
if co:
    print("+ New Country added")
else:
    print("- Couldn't add Country")

brand = Brand()
br = brand.add("Default")
if br:
    print("+ New Brand added")
else:
    print("- Couldn't add Brand")
hoster = Hoster()
ho = hoster.add("Default")
if ho:
    print("+ New Hoster added")
else:
    print("- Couldn't add Hoster")
