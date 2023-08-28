from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    project_name: str
    file_name: str
    file_path: str
    width: int
    height: int
    layers_count: int
    status: str