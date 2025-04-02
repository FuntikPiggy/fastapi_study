import json

import uvicorn
from fastapi import FastAPI

from app import models, sample_products


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/users")
def read_users_dict():
    return models.User01(name="John Doe", id=1)


@app.post("/user")
def add_user_to_dict(user: models.User02):
    usr = user.__dict__
    usr.update({"is_adult": user.age >= 18})
    return usr


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


@app.post("/create_user")
def create_user(user: models.UserCreate):
    users01.append(user)
    return user


@app.get("/get_user01")
def get_users01():
    return users01


@app.get("/product/{product_id}")
def read_product(product_id: int):
    for i in sample_products.sample_products:
        if i["product_id"] == product_id:
            return i


@app.get("/products/search")
def read_products(keyword: str, category: str | None = None, limit: int | None = None):
    res = list(filter(lambda x: keyword.lower() in x["name"].lower(), sample_products.sample_products))
    return res[:limit] if limit else res


feedb_db_path = "feedbacks_db.json"
fbacks_db = json_loading(feedb_db_path)
users01: list[models.UserCreate] = []
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=".app")
    # uvicorn.run(app, port=8000, reload=True)
