from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.project import CreateProject
from sqlalchemy.orm import Session
from app.api import deps
from app import crud

router = APIRouter()

@router.post('/c', response_model=CreateProject)
def create_project(*, db: Session = Depends(deps.get_db), project_in: CreateProject) -> Any:
    project = crud.project.create(db, project_in)
    return project
