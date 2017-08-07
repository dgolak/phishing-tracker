# -*- coding: utf-8 -*-
"""CountryController.py."""
from flask import render_template

from classes.Country import Country


class CountryController(Country):
    """Class BrandController."""

    def __init__(self):
        """init."""
        self.Country = Country()

    def showall(self):
        """showall."""
        arr = self.Country.getall()
        return render_template(
            'index.html',
            arrPhishing=arr
        )

    def add(self):
        """add."""
        pass
