#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-05 10:28:27
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from typing import Optional
from app.cloud_scheduler import schemas
from google.cloud import scheduler_v1


# =========[ Create ]=========

def create_cloud_scheduler_job(
    project_id: str,
    location: str,
    job: schemas.CloudSchedulerJobIn
):
    client = get_cloud_scheduler_client()

    http_target = scheduler_v1.HttpTarget(
        uri=job.http_target.uri,
        http_method=job.http_target.http_method.value,
    )

    if job.http_target.headers:
        http_target.headers = job.http_target.headers
    
    if job.http_target.body:
        http_target.body = job.http_target.body

    job_to_create = scheduler_v1.Job(
        name=f"projects/{project_id}/locations/{location}/jobs/{job.name}",
        description=job.description,
        http_target=http_target,
        schedule=job.schedule,
        time_zone=job.time_zone,
    )

    request = scheduler_v1.CreateJobRequest(
        parent=f"projects/{project_id}/locations/{location}",
        job=job_to_create,
    )

    response = client.create_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)



# =========[ Read ]=========

def get_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.GetJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}"
    )

    response = client.get_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)

# =========[ Update ]=========

def pause_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.PauseJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}"
    )

    response = client.pause_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)


def resume_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.ResumeJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}"
    )

    response = client.resume_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)


def run_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.RunJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}"
    )

    response = client.run_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)


def update_cloud_scheduler_job(
    project_id: str,
    location: str,
    job_id: str,
    job: schemas.CloudSchedulerJobUpdate
):
    client = get_cloud_scheduler_client()

    http_target = scheduler_v1.HttpTarget(
        uri=job.http_target.uri,
        http_method=job.http_target.http_method.value,
    )

    if job.http_target.headers:
        http_target.headers = job.http_target.headers
    
    if job.http_target.body:
        http_target.body = job.http_target.body
    
    job_to_update = scheduler_v1.Job(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
        description=job.description,
        http_target=http_target,
        schedule=job.schedule,
        time_zone=job.time_zone,
    )

    request = scheduler_v1.UpdateJobRequest(
        job=job_to_update,
    )

    response = client.update_job(request=request)

    return proto_obj_to_dict(scheduler_v1.Job, response)


# =========[ List ]=========

def list_cloud_scheduler_jobs(
    project_id: str,
    location: str,
    page_token: Optional[str],
    limit: Optional[int],
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.ListJobsRequest(
        parent=f"projects/{project_id}/locations/{location}",
        page_size=limit,
        page_token=page_token,
    )

    response = client.list_jobs(request=request)._response

    return proto_obj_to_dict(scheduler_v1.ListJobsResponse, response)

# =========[ Delete ]=========

def delete_cloud_scheduler_job(
    project_id: str, 
    location: str, 
    job_id: str
):
    client = get_cloud_scheduler_client()

    request = scheduler_v1.DeleteJobRequest(
        name=f"projects/{project_id}/locations/{location}/jobs/{job_id}",
    )

    response = client.delete_job(request=request)

# =========[ Helpers ]=========

def get_cloud_scheduler_client():
    return scheduler_v1.CloudSchedulerClient()


def proto_obj_to_dict(proto_class, proto_obj):
    return proto_class.to_dict(proto_obj)

