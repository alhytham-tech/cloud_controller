#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-05 10:29:33
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from google.cloud.scheduler_v1 import HttpMethod


class Methods(Enum):
    GET = HttpMethod.GET
    POST = HttpMethod.POST  
    PUT = HttpMethod.PUT
    DELETE = HttpMethod.DELETE
    PATCH = HttpMethod.PATCH
    HEAD = HttpMethod.HEAD
    OPTIONS = HttpMethod.OPTIONS


class CloudSchedulerHttpTarget(BaseModel):
    uri: str = Field(..., description="The URI to send HTTP requests to.")
    http_method: Methods = Field(..., description="The HTTP method to use for requests.")
    headers: Optional[Dict[str, str]] = Field(None, description="The HTTP request headers.")
    body: Optional[bytes] = Field(None, description="The body of the HTTP request.")


class CloudSchedulerJob(BaseModel):
    name: str = Field(..., description="The job name. format: projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID")
    description: Optional[str] = Field(None, description="The job description.")
    http_target: CloudSchedulerHttpTarget = Field(..., description="The target to send the job notifications to.")
    schedule: str = Field(..., description="The cron schedule string defining when the job should run.")
    time_zone: str = Field(..., description="See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.")
    schedule_time: Optional[datetime] = Field(None, description="The next time the job is scheduled to run.")
    last_attempt_time: Optional[datetime] = Field(None, description="The last time this job ran.")


class CloudSchedulerJobIn(BaseModel):
    name: str = Field(..., description="The job name")
    description: Optional[str] = Field(None, description="The job description.")
    http_target: CloudSchedulerHttpTarget = Field(..., description="The target to send the job notifications to.")
    schedule: str = Field(..., description="The cron schedule string defining when the job should run.")
    time_zone: str = Field(..., description="See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.")


class CloudSchedulerJobUpdate(BaseModel):
    name: str = Field(..., description="The job name")
    description: Optional[str] = Field(None, description="The job description.")
    http_target: CloudSchedulerHttpTarget = Field(..., description="The target to send the job notifications to.")
    schedule: str = Field(..., description="The cron schedule string defining when the job should run.")
    time_zone: str = Field(..., description="See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones.")


class CloudSchedulerJobList(BaseModel):
    jobs: Optional[List[CloudSchedulerJob]] = Field(None, description="The list of jobs.")
    next_page_token: Optional[str] = Field(None, description="The next page token.")

