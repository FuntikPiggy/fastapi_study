from pydantic import BaseModel


# Создаём модель данных, которая обычно располагается в файле models.py
class User01(BaseModel):
    id: int
    name: str = ""


class User02(BaseModel):
    name: str = ""
    age: int


class Feedback(BaseModel):
    name: str
    message: str
