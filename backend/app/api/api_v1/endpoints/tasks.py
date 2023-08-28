from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.task import TaskBase
from sqlalchemy.orm import Session
from app.api import deps
from app import crud


router = APIRouter()

@router.post('/c', response_model=TaskBase)
def create_task(*, db: Session = Depends(deps.get_db), task_in: TaskBase) -> Any:
    task = crud.task.create(db, task_in)
    return task