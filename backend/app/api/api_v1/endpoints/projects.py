from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.project import ProjectBase
from sqlalchemy.orm import Session
from app.api import deps
from app import crud

router = APIRouter()

@router.post('')
def get_all_projects(stroka: str) -> Any:
    return {'stroka':stroka}

@router.post('/c', response_model=ProjectBase)
def create_project(*, db: Session = Depends(deps.get_db), project_in: ProjectBase) -> Any:
    project = crud.project.create(db, project_in)
    return project


@router.get('/g', response_model=ProjectBase)
def get_project(*, db: Session = Depends(deps.get_db), name:str) -> Any:
    project = crud.project.get_by_name(db, name)
    return project

@router.put('/u', response_model=ProjectBase)
def update_project(*, db: Session = Depends(deps.get_db), project_in:ProjectBase) -> Any:
    project = crud.project.get_by_name(db, project_in.name)
    crud.project.update(db, project, project_in)
    return project

@router.delete('/d')
def delete_project(*, db: Session = Depends(deps.get_db), name:str) -> Any:
    crud.project.delete_by_name(db, name)