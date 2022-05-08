#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2022-05-03 13:58:30
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class MemorySize(str, Enum):
    _128M = "128Mi"
    _256M = "256Mi"
    _512M = "512Mi"
    _1GiB = "1Gi"
    _2GiB = "2Gi"
    _4GiB = "4Gi"
    _8GiB = "8Gi"
    _16GiB = "16Gi"
    _32GiB = "32Gi"


class CPUType(str, Enum):
    one = "1"
    two = "2"
    four = "4"
    six = "6"
    eight = "8"


class CloudRunAutoScale(BaseModel):
    min_container_count: Optional[int] = Field(..., description="Number of containers to scale the service to")
    max_container_count: Optional[int] = Field(300, description="Maximum number of containers")
    cpu_always_on: Optional[bool] = Field(False, description="whether cpu is always on")
    memory_size: Optional[MemorySize] = Field(None, description="RAM specification")
    cpu_type: Optional[CPUType] = Field(None, description="CPU Type")
    concurrency: Optional[int] = Field(None, description="Maximum request per container")

class CloudRunRevisionScaling(BaseModel):
    min_instance_count: int
    max_instance_count: int


class EnvVar(BaseModel):
    name: str
    value: str


class ContainerPort(BaseModel):
    name: Optional[str] = Field(None)
    container_port: int = Field(..., gt=0, le=65535)


class CloudRunResourceRequirements(BaseModel):
    limits: Optional[Dict[str, str]] = Field(None, description="Only memory and CPU are supported. Note: The only supported values for CPU are '1', '2', and '4'. Setting 4 CPU requires at least 2Gi of memory.")
    cpu_idle: Optional[bool] = Field(None, description="Determines whether CPU should be throttled or not outside of requests.")


class Container(BaseModel):
    name: str
    image: str
    command: List[str]
    args: List[str]
    env: List[EnvVar]
    ports: List[ContainerPort]
    resources: CloudRunResourceRequirements


class CloudRunRevisionTemplate(BaseModel):
    revision: str
    labels: dict
    annotations: dict
    scaling: CloudRunRevisionScaling
    container_concurrency: int
    service_account: str
    containers: List[Container]


class CloudRunService(BaseModel):
    name: str
    description: Optional[str] = None
    uid: str
    generation: int
    labels: dict
    create_time: datetime
    update_time: datetime
    uri: str
    creator: str
    template: CloudRunRevisionTemplate


class CloudRunServiceList(BaseModel):
    services: List[CloudRunService]
    next_page_token: Optional[str]



class CloudRunRevisionScalingUpdate(BaseModel):
    min_instance_count: Optional[int] = Field(None)
    max_instance_count: Optional[int] = Field(None)


class CloudRunRevision(BaseModel):
    name: str
    uid: str
    generation: int
    labels: dict
    create_time: datetime
    update_time: datetime
    service: str
    scaling: CloudRunRevisionScaling
    container_concurrency: int
    service_account: str
    containers: List[Container]
    log_uri: str


class CloudRunRevisionList(BaseModel):
    revisions: List[CloudRunRevision]
    next_page_token: Optional[str]

