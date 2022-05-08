#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-08 01:26:58
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi import FastAPI
from os import getenv
import json

from app.access_control import router as access_control_router
from app.user import router as users_router
from app.dashboard import router as dashboard_router
from app.cloud_run import router as cloud_run_router
from app.cloud_scheduler import router as cloud_scheduler_router

load_dotenv()

app = FastAPI()


origins = json.loads(getenv("ALLOWED_ORIGINS", default=""))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include Routers
app.include_router(users_router.auth_router)
app.include_router(access_control_router.perms_router)
app.include_router(access_control_router.roles_router)
app.include_router(access_control_router.groups_router)
app.include_router(users_router.users_router)
app.include_router(dashboard_router.dashboard_router)
app.include_router(cloud_run_router.service_router)
app.include_router(cloud_run_router.revision_router)
app.include_router(cloud_scheduler_router.job_router)
