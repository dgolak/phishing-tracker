# -*- coding: utf-8 -*-
"""PhishtankModel.py."""

from database import Base

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Integer,
    String,
    func
)


class PhishtankModel(Base):
    """PhishtankModel."""

    __tablename__ = 'Phishtank'
    id = Column(Integer, primary_key=True)
    url = Column(String(200), unique=True)
    urlstatus = Column(Enum("new", "added", "error"), default="new")
    dateadded = Column(DateTime, default=func.now())

    def __init__(
        self,
        url=None,
        urlstatus=None
    ):
        """init."""
        self.url = url
        self.urlstatus = urlstatus

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %r]' % (
            self.id,
            self.url,
            self.urlstatus,
            self.dateadded
        )
