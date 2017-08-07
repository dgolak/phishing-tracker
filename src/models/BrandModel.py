# -*- coding: utf-8 -*-
"""BrandModel.py."""

from database import Base

from sqlalchemy import (
    Column,
    Integer,
    String
)


class BrandModel(Base):
    """BrandModel."""

    __tablename__ = 'Brand'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    email = Column(String(128))
    www = Column(String(128))

    def __init__(
        self,
        name=None,
        email=None,
        www=None
    ):
        """init."""
        self.name = name
        self.email = email
        self.www = www

    def __repr__(self):
        """repr."""
        return '[%d, %r, %r, %r]' % (
            self.id,
            self.name,
            self.email,
            self.www
        )
