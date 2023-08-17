from fastapi import FastAPI, APIRouter

from fastapi.responses import FileResponse

from app.schemas.User import User, UserCreate
from app.schemas.Feedback import Feedback

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


# data = {'name': "John Doe", 'id': 1}

# joe = User(**data)

@api_router.get("/", status_code=200)
def root():
    return FileResponse('app/index.html')


@api_router.post("/calculate")
def calculate(num1:int, num2:int) -> dict:
    return {'result': num1+num2}

@api_router.post('/user')
def get_users(user:User):
    return {'name':user.name,
            'age': user.age,
            'is_adult': user.age>18}

@api_router.post('/feedback')
def feedback(feedb:Feedback):
    return {"message": f'Feedback received. Thank you, {feedb.name}!'}


@api_router.post('/create_user')
def create_user(new_user:UserCreate) -> UserCreate:
    return new_user


app.include_router(api_router)