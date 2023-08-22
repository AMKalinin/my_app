from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import CreateProject

class CRUDProject():
    def create(self, db:Session, project_in:CreateProject)->Project:
        db_project = Project(name = project_in.name,
                             create_date = project_in.create_date,
                             last_update_date = project_in.last_update_date,
                             creator = project_in.creator,
                             status = project_in.status,
                             description = project_in.description)
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

project = CRUDProject() 
    