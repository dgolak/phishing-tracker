# -*- coding: utf-8 -*-
"""Brand.py."""
from database import db_session

from models.BrandModel import BrandModel


class Brand(BrandModel):
    """Brand."""

    def getall(self):
        """getall."""
        r = db_session.execute("""
            select * from Brand
            """)
        return r

    def add(self, name=None, email=None, www=None):
        """add."""
        newbrand = BrandModel(
            name=name,
            email=email,
            www=www
        )
        try:
            db_session.add(newbrand)
            db_session.commit()
            r = newbrand.id
        except:
            r = False
        db_session.close()
        return r
