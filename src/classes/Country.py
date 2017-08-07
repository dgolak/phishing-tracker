# -*- coding: utf-8 -*-
"""Country.py."""
from database import db_session

from models.CountryModel import CountryModel


class Country(CountryModel):
    """Country."""

    def getall(self):
        """getall."""
        r = db_session.execute("""
            select * from Country
            """)
        return r

    def getcountryid(self, shortname):
        """getcountry."""
        print(":::::::::")
        print(shortname)
        countryexist = CountryModel.query.filter(
            CountryModel.shortname == shortname
        ).first()
        if countryexist:
            return countryexist.id
        return False

    def add(self, name='Temporary', shortname='tmp'):
        """add."""
        countryexistid = self.getcountryid(shortname)
        if countryexistid > 0:
            print("COUNTRY JEST"+str(countryexistid))
            return countryexistid
        else:
            print("NIE MA COUNTRY")
            newcountry = CountryModel(
                name=name,
                shortname=shortname
            )
            try:
                db_session.add(newcountry)
                db_session.commit()
                r = newcountry.id
            except:
                r = False
                print("Could'n add Country")
            db_session.close()
            return r
