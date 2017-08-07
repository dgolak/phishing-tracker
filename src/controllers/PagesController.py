# -*- coding: utf-8 -*-
"""PagesController."""

from flask import render_template


class PagesController():
    """Class PagesController."""

    def __init__(self):
        """init."""

    def about(self):
        """about."""
        return render_template(
            'pages/about.html'
        )

    def contact(self):
        """contact."""
        return render_template(
            'pages/contact.html'
        )

    def donate(self):
        """donate."""
        return render_template(
            'pages/donate.html'
        )
