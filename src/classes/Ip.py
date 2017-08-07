# -*- coding: utf-8 -*-
"""Ip.py."""

from database import db_session
from models.IpModel import IpModel
from models.HosterModel import HosterModel
from classes.Country import Country
from ipwhois import IPWhois
import random
from sqlalchemy import and_


class Ip(IpModel):
    """Ip."""

    def getall(self):
        """getall."""
        r = db_session.execute("""
            select * from Ip
            """)
        return r

    def add(self, ip, hoster=1, country=1):
        """add."""
        newip = IpModel(
            ip=ip,
            hoster=hoster,
            country=country
        )
        try:
            db_session.add(newip)
            db_session.commit()
            r = newip.id
        except:
            r = False
        return r

    def updateip(self, id, ip):
        """updateip."""
        ipm = IpModel.query.filter_by(id=id).first()
        ipm.ip = ip
        r = db_session.commit()
        print(r)

    def getdrandomonewithdefaulthoster(self):
        """getrandomonewithdefaulthoster."""
        iparr = db_session.query(
            IpModel,
            HosterModel
        ).join(HosterModel).filter(
            and_(
                HosterModel.name == 'Default',
                IpModel.ip != '1.1.1.3',
                IpModel.ip != '127.0.0.1'
            )
        ).all()
        if len(iparr) > 0:
            rand = random.randint(0, int(len(iparr) - 1))
            return iparr[rand]
        else:
            return False

    def getwhoisdata(self, ip):
        """getwhoisdata."""
        ret = {}
        obj = IPWhois(ip)
        res = obj.lookup_whois()
        ret['asn'] = res['asn']
        hostername = res['nets'][0]['name']
        if res['nets'][0]['country'] is "False":
            print("TU JEST COUNTRY FALSE: " + str(res['nets'][0]['country']))
            country = "False"
        else:
            country = res['nets'][0]['country']
            print("TU NIE MA COUNTRY TRUE")
        cnt = Country()
        ret['country'] = cnt.add(name='some', shortname=country)
        ret['hostername'] = hostername
        return ret
