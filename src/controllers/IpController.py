# -*- coding: utf-8 -*-
"""IpController.py."""

from classes.Ip import Ip

from flask import render_template
from database import db_session
from classes.Hoster import Hoster


class IpController(Ip):
    """IpController."""

    def __init__(self):
        """init."""
        self.ip = Ip()

    def updatephishingip(self):
        """updatephishingip."""
        self.ip.getrandomonewithdefaultip()
        return render_template(
            'update.html'
        )

    def updatehoster(self):
        """ipupdatehoster."""
        wh = self.ip.getdrandomonewithdefaulthoster()
        if wh:
            print(wh[0].ip)
            ret = self.ip.getwhoisdata(wh[0].ip)
            print("++++++++++++++++++++++++")
            print(ret)
            print(ret['country'])
            if ret['hostername'] is "False":
                print("HOSTER:TU JEST FALSE: " + str(ret['hostername']))
                hoster = "False"
            else:
                hoster = ret['hostername']
                print("HOSTER:TU NIE MA TRUE" + str(ret['hostername']))
            hst = Hoster()
            ret['hoster'] = hst.add(name=hoster, email='dawid@wp.pl')
            # print("HOSTER ID="+str(ret['hoster']))
            wh[0].country = ret['country']
            wh[0].hoster = ret['hoster']
            wh[0].asn = ret['asn']
            print("------- obiekt przed update")
            print(wh[0])
            db_session.commit()
            db_session.close()

        print("Robimy update IP")
        return render_template(
            'update.html'
        )
