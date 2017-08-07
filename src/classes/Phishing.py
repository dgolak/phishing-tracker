# -*- coding: utf-8 -*-
"""Phishing.py."""

from database import db_session

from models.PhishingModel import PhishingModel
from models.IpModel import IpModel
import random
import datetime


class Phishing(PhishingModel):
    """Phishing."""

    def getall(self):
        """getall."""
        arr = Phishing.query.all()
        return arr

    def yesterday(self):
        """yesterday."""
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d")

    def getall2map(self):
        """getall2map."""
        r = db_session.execute("""
            select I.*,c.id, c.symbol, c.name, c.shortname,
            count(c.shortname) AS cnt
            FROM Ip AS I LEFT JOIN country AS C ON (C.id=I.country)
            LEFT JOIN Phishing AS P ON (P.ip=I.id)
            WHERE P.phishingstatus !='running'
            AND P.dateadded >= '{}'
            GROUP BY(c.shortname);
            """.format(self.yesterday()))
        return r

    def getall2brands(self):
        """getall2map."""
        r = db_session.execute("""
            select I.*,c.id, c.symbol, c.name, c.shortname,
            count(c.shortname) AS cnt
            FROM Ip AS I LEFT JOIN country AS C ON (C.id=I.country)
            LEFT JOIN Phishing AS P ON (P.ip=I.id)
            WHERE P.phishingstatus !='running'
            GROUP BY(c.shortname);
            """)
        return r

    def getid(self, url):
        """getid."""
        p = PhishingModel.query.filter_by(url=url).first()
        if p:
            return p.id
        return False

    def add(self, url, brand=1, ip=1, status='added'):
        """add."""
        phishid = self.getid(url)
        if phishid < 1:
            newphishing = PhishingModel(
                url=url,
                brand=brand,
                ip=1,
                phishingstatus=status
            )
            try:
                db_session.add(newphishing)
                db_session.commit()
                ret = newphishing.id
            except:
                print("I can'n add new phishing")
                ret = False
            return ret
        else:
            return phishid

    def updateip(self, phishid, ipid):
        """updateip."""
        phish = PhishingModel.query.filter_by(id=phishid).first()
        phish.ip = ipid
        db_session.commit()
        db_session.close()

    def getrandomonewithdefaultip(self, ip='1.1.1.3'):
        """getrandomonewithdefaultip."""
        iparr = db_session.query(
            PhishingModel,
            IpModel
        ).join(IpModel).filter_by(ip='1.1.1.3').all()
        if len(iparr) > 0:
            rand = random.randint(0, int(len(iparr) - 1))
            return iparr[rand]
        else:
            return False
