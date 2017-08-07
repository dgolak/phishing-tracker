# -*- coding: utf-8 -*-
"""PhishingModel.py."""

from classes.Brand import Brand

from classes.Ip import Ip

from database import Base

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    func
)


class PhishingModel(Base):
    """PhishingModel."""

    __tablename__ = 'Phishing'
    id = Column(Integer, primary_key=True)
    url = Column(String(200), unique=True)
    brand = Column(Integer, ForeignKey(Brand.id))
    ip = Column(Integer, ForeignKey(Ip.id))
    dateadded = Column(DateTime, default=func.now())
    phishingstatus = Column(Enum("added", "verified", "running", "deleted"))
    statusdate = Column(DateTime, default=func.now())

    def __init__(
        self,
        url=None,
        brand=None,
        ip=None,
        phishingstatus=None
    ):
        """init."""
        self.url = url
        self.brand = brand
        self.ip = ip
        self.phishingstatus = phishingstatus

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %d, %r, %r, %r]' % (
            self.id,
            self.url,
            self.brand,
            self.ip,
            self.dateadded,
            self.phishingstatus,
            self.statusdate
        )
