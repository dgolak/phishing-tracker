# -*- coding: utf-8 -*-
"""Phishtank.py."""

import re
import requests
import sys

from database import db_session

from models.PhishtankModel import PhishtankModel


class Phishtank(PhishtankModel):
    """Phishtank."""

    def getallurl(self):
        """getallurl."""
        print("Laczymy sie z phishtank")
        try:
            r = requests.get("http://www.phishtank.com/phish_archive.php")
        except:
            print("Failed to connect Phishtank.com")
        return self.geturl(r.text)

    def getdetails(self, url):
        """getdetails."""
        try:
            r = requests.get(url)
            print(r.status_code)
        except:
            print("Failed to connect Phishtank.com")
        return self.geturl(r.text)

    def geturl(self, content):
        """geturl."""
        x = re.findall(r'\?phish_id=([0-9]+)">', content)
        return x

    def add(self, url, urlstatus='new'):
        """add."""
        newphishtank = PhishtankModel(
            url=url,
            urlstatus=urlstatus
        )
        try:
            db_session.add(newphishtank)
            db_session.commit()
            db_session.close()
            return newphishtank
        except:
            db_session.close()
            return False

    def deleteone(self, phishtankid):
        """deleteone."""
        PhishtankModel.query.filter_by(id=phishtankid).delete()
        db_session.commit()

    def getone(self):
        """getone."""
        r = PhishtankModel.query.filter_by(urlstatus='new').first()
        return r

    def getphishingurl(self, ph):
        """getphishingurl."""
        try:
            r = requests.get(ph)
        except:
            print("Failed to connect Phishtank.com")
        try:
            x = re.findall(r'<b>(.*)</b>', r.text)
        except:
            print("Lack of the url in regexp")
            sys.exit()
        return x[1]

    def updatestatus(self, ph_id, status='new'):
        """updatestatus."""
        p = PhishtankModel.query.filter_by(id=ph_id).first()
        p.urlstatus = status
        try:
            db_session.commit()
        except:
            pass
