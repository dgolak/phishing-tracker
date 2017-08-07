# -*- coding: utf-8 -*-
"""PhishtankController.py."""

from classes.Ip import Ip
from classes.Phishing import Phishing
from classes.Phishtank import Phishtank
from urllib.parse import urlparse

from flask import render_template
import socket


class PhishtankController(Phishtank):
    """PhishtankController."""

    def __init__(self):
        """init."""
        pass

    def getallurlfromphishtank(self):
        """getallurlfromphishtank."""
        phishtank = Phishtank()
        r = phishtank.getallurl()
        if len(r) > 0:
            for i in r:
                phishtank.add(
                    'http://www.phishtank.com/phish_detail.php?phish_id=' +
                    str(i)
                )
        return render_template(
            'update.html',
            arrPhishing="asd"
        )

    def goodnetloc(self, netloc):
        """goodnetloc."""
        try:
            socket.gethostbyname(netloc)
            return True
        except:
            return False

    def getphishtankandaddphishing(self):
        """getphishtankandaddphishing."""
        phishtank = Phishtank()
        r = None
        try:
            r = phishtank.getone()
        except:
            pass
        if r:
            phishingurl = phishtank.getphishingurl(r.url)
            u = urlparse(phishingurl)
            print(self.goodnetloc(u.netloc))
            if self.goodnetloc(u.netloc) is True:
                pass
            else:
                print("Phishing domain is not validated" + str(phishingurl))
                phishtank.deleteone(r.id)
                import sys
                sys.exit()
            phishing = Phishing()
            ph_id = phishing.add(phishingurl)
            if ph_id > 0:
                phishtank.updatestatus(r.id, 'added')
                ip = Ip()
                newipid = ip.add('1.1.1.3')
                phishing.updateip(ph_id, newipid)
            else:
                phishtank.updatestatus(r.id, 'error')
        return render_template(
            'phishtank/getandaddone.html'
        )
