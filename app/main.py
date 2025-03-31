import json

import models
import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/users")
def read_users_dict():
    return models.User(name="John Doe", id=1)


@app.post("/user")
def add_user_to_dict(user: models.User):
    usr = user.__dict__
    usr.update({"is_adult": user.age >= 18})
    return usr
    # return {"name": user.name,
    #         "age": user.age,
    #         "is_adult": user.age>=18}


def json_dumping(path: str, feed_db: dict) -> None:
    with open(path, "w", encoding="U8") as ofl:
        json.dump(feed_db, ofl, indent=4, ensure_ascii=False, separators=(",", ": "))


def json_loading(path: str) -> dict:
    try:
        with open(path, "r", encoding="U8") as ifl:
            return json.load(ifl)
    except Exception:
        return {"feedbacks": []}


@app.post("/feedback")
def post_feedback(feedback: models.Feedback):
    global feedb_db_path
    fbacks_db["feedbacks"].append(feedback.__dict__)
    json_dumping(feedb_db_path, fbacks_db)
    return {"message": f"Feedback received. Thank you, {feedback.name}!"}


feedb_db_path = "feedbacks_db.json"
fbacks_db = json_loading(feedb_db_path)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=".app")
    # uvicorn.run(app, port=8000, reload=True)
