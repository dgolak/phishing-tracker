# -*- coding: utf-8 -*-
"""database.py."""

import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


time.sleep(1)

print("Connect to database")


engine = create_engine(
    "sqlite:////tmp/p.db",
    convert_unicode=True,
    isolation_level="READ UNCOMMITTED"
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """init_db."""
    Base.metadata.create_all(bind=engine)
