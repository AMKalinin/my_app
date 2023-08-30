from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.project import ProjectBase
from sqlalchemy.orm import Session
from app.api import deps
from app import crud

router = APIRouter()

@router.get('', response_model=list[ProjectBase])
def get_all_projects(db: Session = Depends(deps.get_db)) -> Any:
    return crud.project.get_all(db)

@router.post('/create', response_model=ProjectBase)
def create_project(*, db: Session = Depends(deps.get_db), project_in: ProjectBase) -> Any:
    project = crud.project.create(db, project_in)
    return project

@router.post('/create-based', response_model=ProjectBase)
def create_project(*, db: Session = Depends(deps.get_db), project_in: ProjectBase) -> Any:
    ...

@router.get('/{project_name}', response_model=ProjectBase)
def get_project(*, db: Session = Depends(deps.get_db), project_name:str) -> Any:
    project = crud.project.get_by_name(db, project_name)
    return project

@router.delete('/{project_name}')
def delete_project(*, db: Session = Depends(deps.get_db), project_name:str) -> Any:
    crud.project.delete_by_name(db, project_name)
