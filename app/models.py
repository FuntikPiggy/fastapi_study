from datetime import datetime

from pydantic import BaseModel


# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    # id: int
    name: str = ""
    age: int


class Feedback(BaseModel):
    name: str
    message: str
