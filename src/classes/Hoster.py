# -*- coding: utf-8 -*-
"""Phishing.py."""
from database import db_session

from models.HosterModel import HosterModel


class Hoster(HosterModel):
    """Hoster."""

    def getall(self):
        """getall."""
        r = db_session.execute("""
            select * from Hoster
            """)
        return r

    def gethosterid(self, name):
        """gethosterid."""
        print(":::::::::")
        print(name)
        hosterexist = HosterModel.query.filter(
            HosterModel.name == name
        ).first()
        if hosterexist:
            return hosterexist.id
        return False

    def add(self, name=None, www=None, email=None):
        """add."""
        hosterexistid = self.gethosterid(name)
        if hosterexistid > 0:
            print("HOSTER JEST"+str(hosterexistid))
            return hosterexistid
        else:
            newhoster = HosterModel(
                name=name,
                www=www,
                email=email
            )
            #try:
            if 1:
                db_session.add(newhoster)
                db_session.commit()
                r = newhoster.id
            #except:
                r = False
            db_session.close()
        return r
