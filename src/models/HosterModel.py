# -*- coding: utf-8 -*-
"""HosterModel.py."""

from database import Base

from sqlalchemy import (
    Column,
    Integer,
    String
)


class HosterModel(Base):
    """HosterModel."""

    __tablename__ = 'Hoster'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    www = Column(String(128))
    email = Column(String(128))

    def __init__(
        self,
        name=None,
        www=None,
        email=None
    ):
        """init."""
        self.name = name
        self.www = www
        self.email = email

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %r]' % (
            self.id,
            self.name,
            self.www,
            self.email
        )
