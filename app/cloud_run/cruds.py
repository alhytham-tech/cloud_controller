#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-03 14:05:39
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from typing import Optional
from app.cloud_run import schemas
from google.cloud import run_v2


# =========[ Create ]=========


# =========[ Read ]=========

def get_raw_cloud_run_service(
    project_id: str, 
    location: str, 
    service_id: str
):
    client = get_cloud_run_service_client()

    request = run_v2.GetServiceRequest(
        name=f"projects/{project_id}/locations/{location}/services/{service_id}"
    )

    return client.get_service(request=request)


def get_cloud_run_service(
    project_id: str, 
    location: str, 
    service_id: str
):
    response = get_raw_cloud_run_service(project_id, location, service_id)
    return proto_obj_to_dict(run_v2.Service, response)
    
# =========[ Update ]=========

def auto_scale_cloud_run_service(
    project_id: str,
    location: str,
    service_id: str,
    auto_scale: schemas.CloudRunAutoScale
):
    service: run_v2.Service = get_raw_cloud_run_service(project_id, location, service_id)

    revision_scaling = run_v2.RevisionScaling()
    revision = run_v2.RevisionTemplate()
    
    if auto_scale.min_container_count:
        revision_scaling.min_instance_count = auto_scale.min_container_count
        revision_scaling.max_instance_count = auto_scale.max_container_count
    
    if auto_scale.concurrency:
        revision.container_concurrency = auto_scale.concurrency
    
    if auto_scale.cpu_type:
        service.template.containers[0].resources.limits["cpu"] = auto_scale.cpu_type
    
    if auto_scale.memory_size:
        service.template.containers[0].resources.limits["memory"] = auto_scale.memory_size
    
    service.template.containers[0].resources.cpu_idle = not auto_scale.cpu_always_on
    
    revision.scaling = revision_scaling
    revision.containers = service.template.containers

    client = get_cloud_run_service_client()

    to_update = run_v2.Service(
        name=service.name,
        template=revision,
    )

    request = run_v2.UpdateServiceRequest(
        service=to_update,
    )

    response = client.update_service(request=request).result()

    return proto_obj_to_dict(run_v2.Service, response)


# =========[ List ]=========

def list_cloud_run_services(
    project_id: str, 
    location: str,
    page_token: Optional[str],
    limit: Optional[int],
):
    client = get_cloud_run_service_client()
    
    request = run_v2.ListServicesRequest(
        parent=f"projects/{project_id}/locations/{location}",
        page_size=limit,
        page_token=page_token,
    )

    response = client.list_services(request=request)._response
    return proto_obj_to_dict(run_v2.ListServicesResponse, response)


def list_cloud_run_revisions(
    project_id: str, 
    location: str, 
    service_id: str, 
    page_token: Optional[str], 
    limit: Optional[int]
):
    client = get_cloud_run_revision_client()

    request = run_v2.ListRevisionsRequest(
        parent=f"projects/{project_id}/locations/{location}/services/{service_id}",
        page_size=limit,
        page_token=page_token,
    )

    response = client.list_revisions(request=request)._response
    return proto_obj_to_dict(run_v2.ListRevisionsResponse, response)


# =========[ Delete ]=========


# =========[ Helpers ]=========

def get_cloud_run_service_client():
    return run_v2.ServicesClient()


def get_cloud_run_revision_client():
    return run_v2.RevisionsClient()


def proto_obj_to_dict(proto_class, proto_obj):
    return proto_class.to_dict(proto_obj)