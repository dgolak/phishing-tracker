# -*- coding: utf-8 -*-
"""CountryModel.py."""

from database import Base

from sqlalchemy import (
    Column,
    Integer,
    String
)


class CountryModel(Base):
    """CountryModel."""

    __tablename__ = 'Country'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    shortname = Column(String(3), unique=True)
    symbol = Column(String(3))

    def __init__(
        self,
        name=None,
        shortname=None,
        symbol=None
    ):
        """init."""
        self.name = name
        self.shortname = shortname
        self.symbol = symbol

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %r]' % (
            self.id,
            self.name,
            self.shortname,
            self.symbol
        )
