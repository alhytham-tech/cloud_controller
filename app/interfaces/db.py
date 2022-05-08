#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-09 13:58:44
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from app.mixins.columns import BaseUACMixin


class DBModel(BaseUACMixin):
    """
    an attempt to create interface and editor support for
    for models typed with this class
    """
    nin: str
    email: str
