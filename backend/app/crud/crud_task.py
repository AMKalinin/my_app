from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskBase

class CRUDTask():
    def create(self, db:Session, task_in:TaskBase)->Task:
        db_task = Task(id=task_in.id,
                        project_name=task_in.project_name,
                        file_name=task_in.file_name,
                        width=task_in.width,
                        height=task_in.height,
                        layers_count=task_in.layers_count,
                        status=task_in.status)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task


task = CRUDTask() 