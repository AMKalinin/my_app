from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.task import TaskBase
from sqlalchemy.orm import Session
from app.api import deps
from app import crud


router = APIRouter()

@router.get('')
def get_all_tasks_in_project(project_name:str):
    ...

@router.get('/{task_id}')
def get_task(project_name:str, task_id:int):
    ...

@router.put('/{task_id}')
def update_task_status(project_name:str, task_id:int):
    ...