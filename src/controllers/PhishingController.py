# -*- coding: utf-8 -*-
"""PhishingController.py."""
from classes.Phishing import Phishing

from flask import render_template

from urllib.parse import urlparse
from classes.Ip import Ip
# from classes.Malcante import Malcante
import socket


class PhishingController(Phishing):
    """Class PhishingController."""

    def __init__(self):
        """init."""
        self.phishing = Phishing()

    def showall(self):
        """showall."""
        arr = self.phishing.getall2map()
        # last = self.malcante.getlast(5)
        return render_template(
            'index.html',
            arrPhishing=arr,
            # lastPhishing=last
        )

    def showall2brands(self):
        """showall2brands."""
        arr = self.phishing.getall2brands()
        return render_template(
            'phishing/brands.html',
            arrPhishing=arr
        )

    def updatephishingip(self):
        """updatephishingip."""
        ip = self.phishing.getrandomonewithdefaultip()
        # print("__----___---____--_____---___---____")
        # print(ip)
        # print("__----___---____--_____---___---____")
        if ip:
            u = urlparse(ip[0].url)
            try:
                domainip = socket.gethostbyname(u.netloc)
                ipm = Ip()
                ipm.updateip(ip[1].id, domainip)
            except:
                print("I can't get host ip" + str(u.netloc))
        return render_template(
            'update.html',
            msg="updatephishingip: I can't get host ip" + str(u.netloc)
        )
