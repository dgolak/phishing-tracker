# -*- coding: utf-8 -*-
"""IpModel.py."""
from models.HosterModel import HosterModel
from models.CountryModel import CountryModel

from database import Base

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)


class IpModel(Base):
    """IpModel."""

    __tablename__ = 'Ip'
    id = Column(Integer, primary_key=True)
    ip = Column(String(16))
    hoster = Column(Integer, ForeignKey(HosterModel.id))
    country = Column(Integer, ForeignKey(CountryModel.id))
    asn = Column(String(16))

    def __init__(
        self,
        ip=None,
        hoster=None,
        country=None,
        asn=None
    ):
        """init."""
        self.ip = ip
        self.hoster = hoster
        self.country = country
        self.asn = asn

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %r, %r]' % (
            self.id,
            self.ip,
            self.hoster,
            self.country,
            self.asn
        )
