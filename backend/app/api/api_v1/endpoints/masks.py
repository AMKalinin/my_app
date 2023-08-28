from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.mask import MaskBase
from sqlalchemy.orm import Session
from app.api import deps
from app import crud


router = APIRouter()

@router.post('/c', response_model=MaskBase)
def create_task(*, db: Session = Depends(deps.get_db), mask_in: MaskBase) -> Any:
    mask = crud.mask.create(db, mask_in)
    return mask