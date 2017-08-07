# -*- coding: utf-8 -*-
"""page.py."""

from controllers.PhishingController import PhishingController
from controllers.PhishtankController import PhishtankController
from controllers.IpController import IpController
from controllers.PagesController import PagesController


class Page():
    """Page."""

    def __init__(self, app):
        """init."""
        app.add_url_rule('/', 'index', self.defaultpath)
        app.add_url_rule('/phishtank/getall', 'getall', self.phishtankgetall)
        app.add_url_rule('/brands', 'brands', self.phishingbrands)
        app.add_url_rule('/about', 'about', self.pagesabout)
        app.add_url_rule('/donate', 'donate', self.pagesdonate)
        app.add_url_rule('/contact', 'contact', self.pagescontact)
        app.add_url_rule(
            '/phishtank/getandaddone',
            'getandaddone',
            self.phishtankgetandaddone
        )
        app.add_url_rule(
            '/phishing/updatephishingip',
            'updatephishingip',
            self.phishingupdatephishingip
        )
        app.add_url_rule(
            '/ip/updatehoster',
            'updatehoster',
            self.ipupdatehoster
        )

    def pagesabout(self):
        """pagesabout."""
        p = PagesController()
        return p.about()

    def pagesdonate(self):
        """pagesdonate."""
        p = PagesController()
        return p.donate()

    def pagescontact(self):
        """pagescontact."""
        p = PagesController()
        return p.contact()

    def defaultpath(self):
        """default."""
        p = PhishingController()
        return p.showall()

    def phishingbrands(self):
        """phishingbrands."""
        p = PhishingController()
        return p.showall2brands()

    def phishtankgetall(self):
        """phishtankgetall."""
        p = PhishtankController()
        return p.getallurlfromphishtank()

    def phishtankgetandaddone(self):
        """phishtankgetone."""
        p = PhishtankController()
        return p.getphishtankandaddphishing()

    def phishingupdatephishingip(self):
        """phishingupdatephishingip."""
        phip = PhishingController()
        return phip.updatephishingip()

    def ipupdatehoster(self):
        """ipupdatehoster."""
        phip = IpController()
        return phip.updatehoster()
