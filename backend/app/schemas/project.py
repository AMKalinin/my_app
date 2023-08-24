from pydantic import BaseModel
import datetime


class BaseProject(BaseModel):
    name: str
    create_date: datetime.date
    last_update: datetime.date
    creator: str
    status: str
    description: str | None = None
