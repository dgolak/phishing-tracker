# -*- coding: utf-8 -*-
"""PhishingController."""
from classes.Brand import Brand

from flask import render_template


class BrandController(Brand):
    """Class BrandController."""

    def __init__(self):
        """init."""
        self.Brand = Brand()

    def showall(self):
        """showall."""
        arr = self.Brand.getall()
        return render_template(
            'index.html',
            arrPhishing=arr
        )
