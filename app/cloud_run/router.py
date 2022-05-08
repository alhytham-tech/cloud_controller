#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-03 13:12:27
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from typing import Optional
from fastapi import APIRouter, Depends, Query, Path
from app.dependencies.dependencies import HasPermission, get_current_user, get_db
from app.cloud_run import schemas, cruds

service_router = APIRouter(
    prefix="/cloud_run/service",
    tags=["Cloud Run Service Endpoints"],
)

revision_router = APIRouter(
    prefix="/cloud_run/revision",
    tags=["Cloud Run Revision Endpoints"],
)

# ============[ Create Routes]============


# ============[ Read Routes]============

@service_router.get(
    "/view/{project_id}/{location}/{service_id}",
    response_model=schemas.CloudRunService,
    dependencies=[Depends(HasPermission(["can_view_cloud_run_service"]))],
)
async def get_cloud_run_service(
    project_id: str,
    location: str,
    service_id: str,
):
    return cruds.get_cloud_run_service(project_id, location, service_id)


# ============[ Update Routes]============

@service_router.put(
    "/auto_scale/{project_id}/{location}/{service_id}",
    response_model=schemas.CloudRunService,
    dependencies=[Depends(HasPermission(["can_update_cloud_run_service"]))],
)
async def auto_scale_cloud_run_service(
    project_id: str = Path(..., description="Google Cloud Project ID"),
    location: str = Path(..., description="Valid google cloud region"),
    service_id: str = Path(..., description="Service ID"),
    auto_scale: schemas.CloudRunAutoScale = Depends(),
):
    return cruds.auto_scale_cloud_run_service(project_id, location, service_id, auto_scale)


# ============[ List Routes]============

@service_router.get(
    "/list/{project_id}/{location}",
    response_model=schemas.CloudRunServiceList,
    dependencies=[Depends(HasPermission(["can_list_cloud_run_services"]))],
)
async def list_cloud_run_services(
    project_id: str = Path(..., description="Google Cloud Project ID"),
    location: str = Path(..., description="Valid google cloud region"),
    page_token: Optional[str] = Query("", description="Page token received from previous request"),
    limit: Optional[int] = Query(100, description="Number of records to return"),
):
    return cruds.list_cloud_run_services(project_id, location, page_token, limit)


@revision_router.get(
    "/list/{project_id}/{location}/{service_id}",
    response_model=schemas.CloudRunRevisionList,
    dependencies=[Depends(HasPermission(["can_list_cloud_run_revisions"]))],
)
async def list_cloud_run_revisions(
    project_id: str = Path(..., description="Google Cloud Project ID"),
    location: str = Path(..., description="Valid google cloud region"),
    service_id: str = Path(..., description="Service ID"),
    page_token: Optional[str] = Query("", description="Page token received from previous request"),
    limit: Optional[int] = Query(100, description="Number of records to return"),
):
    return cruds.list_cloud_run_revisions(project_id, location, service_id, page_token, limit)


# ============[ Delete Routes]============

