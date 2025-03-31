import uvicorn
from fastapi import FastAPI

from models import models


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/users")
def read_custom_message():
    return models.User(name="John Doe", id=1)


@app.post("/user")
def read_custom_message(user: models.User):
    usr = user.__dict__
    usr.update({"is_adult": user.age >= 18})
    return usr
    # return {"name": user.name,
    #         "age": user.age,
    #         "is_adult": user.age>=18}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=".app")
    # uvicorn.run(app, port=8000, reload=True)
