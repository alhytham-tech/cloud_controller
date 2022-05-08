#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-06 13:46:25
# @Author  : Dahir Muhammad Dahir
# @Description : taken from Bill's template codebase


import ulid

import inflect # type: ignore

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.functions import func


get_plural = inflect.engine()

def get_new_ulid():
    return ulid.new().str

class BaseMixin:
    '''
    Provides id, created_at and last_modified columns
    '''
    @declared_attr
    def __tablename__(cls):
        try:
            table_name = cls.__tablename__
        except RecursionError:
            pass
        plural_name = get_plural.plural_noun(cls.__name__.lower())
        return plural_name

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uuid = Column(String(length=50), unique=True, nullable=False, default=get_new_ulid)
    created_at = Column(DateTime, index=True, server_default=func.now(), nullable=False)
    last_modified = Column( DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


class BaseUACMixin(BaseMixin):
    '''
    Defines common columns for user access control models
    '''
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(255))


class BaseMainMixin:
    '''
    Note: in postgres we don't need id as primary key, uuid works
    Provides id, created_at and last_modified columns
    '''
    @declared_attr
    def __tablename__(cls):
        try:
            table_name = cls.__tablename__
        except RecursionError:
            pass
        plural_name = get_plural.plural_noun(cls.__name__.lower())
        return plural_name

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uuid = Column(String(length=50), unique=True, nullable=False, default=get_new_ulid)
    created_at = Column(DateTime, index=True, server_default=func.now(), nullable=False)
    last_modified = Column( DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

