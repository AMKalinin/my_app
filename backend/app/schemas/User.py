from pydantic import BaseModel, EmailStr, PositiveInt


class User(BaseModel):
    name: str
    age: int

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = None
    is_subscribed: bool | None = None
