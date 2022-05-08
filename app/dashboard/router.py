#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-09-27 08:25:51
# @Author  : Dahir Muhammad Dahir
# @Description : something cool



from app.user.schemas import UserSchema
from fastapi import APIRouter, Depends, Query, Path, Form, File, Body, UploadFile
from sqlalchemy.orm.session import Session
from app.dependencies.dependencies import HasPermission, get_current_user, get_db
from app.dashboard import cruds, schemas


dashboard_router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboards Endpoints"],
)

# ============[ Dashboard Routes]============



