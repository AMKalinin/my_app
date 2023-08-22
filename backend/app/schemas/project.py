from pydantic import BaseModel
import datetime


class CreateProject(BaseModel):
    name: str
    create_date: datetime.date
    last_update: datetime.date
    creator: str
    status: str
    description: str | None = None
