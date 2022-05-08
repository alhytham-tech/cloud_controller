#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-05 10:28:45
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from typing import Optional
from fastapi import APIRouter, Depends, Query
from app.dependencies.dependencies import HasPermission
from app.cloud_scheduler import schemas, cruds


job_router = APIRouter(
    prefix="/cloud_scheduler/job",
    tags=["Cloud Scheduler Job Endpoints"],
)


# ============[ Create Routes]============

@job_router.post(
    "/create/{project_id}/{location}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_create_cloud_scheduler_job"]))],
)
async def create_cloud_scheduler_job(
    project_id: str,
    location: str,
    job: schemas.CloudSchedulerJobIn,
):
    return cruds.create_cloud_scheduler_job(project_id, location, job)

# ============[ Read Routes]============

@job_router.get(
    "/view/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_view_cloud_scheduler_job"]))],
)
async def get_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
):
    return cruds.get_cloud_scheduler_job(project_id, location, job_id)


# ============[ Update Routes]============

@job_router.put(
    "/update/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_update_cloud_scheduler_job"]))],
)
async def update_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
    job: schemas.CloudSchedulerJobUpdate,
):
    return cruds.update_cloud_scheduler_job(project_id, location, job_id, job)


@job_router.put(
    "/run/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_run_cloud_scheduler_job"]))],
)
async def run_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
):
    return cruds.run_cloud_scheduler_job(project_id, location, job_id)


@job_router.put(
    "/pause/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_pause_cloud_scheduler_job"]))],
)
async def pause_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
):
    return cruds.pause_cloud_scheduler_job(project_id, location, job_id)


@job_router.put(
    "/resume/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_resume_cloud_scheduler_job"]))],
)
async def resume_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
):
    return cruds.resume_cloud_scheduler_job(project_id, location, job_id)


# ============[ List Routes]============

@job_router.get(
    "/list/{project_id}/{location}",
    response_model=schemas.CloudSchedulerJobList,
    dependencies=[Depends(HasPermission(["can_list_cloud_scheduler_job"]))],
)
async def list_cloud_scheduler_jobs(
    project_id: str,
    location: str,
    page_token: Optional[str] = Query(None, description="Token for next page"),
    page_size: Optional[int] = Query(10, description="Number of results to return"),
):
    return cruds.list_cloud_scheduler_jobs(project_id, location, page_token, page_size)

# ============[ Delete Routes]============

@job_router.delete(
    "/delete/{project_id}/{location}/{job_id}",
    response_model=schemas.CloudSchedulerJob,
    dependencies=[Depends(HasPermission(["can_delete_cloud_scheduler_job"]))],
)
async def delete_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
):
    return cruds.delete_cloud_scheduler_job(project_id, location, job_id)

