from pydantic import BaseModel, EmailStr, Field, PositiveInt


# Создаём модель данных, которая обычно располагается в файле models.py
class User01(BaseModel):
    id: int
    name: str = ""


class User02(BaseModel):
    name: str = ""
    age: int


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = Field(default=None, lt=130)
    is_subscribed: bool = False


class Product_01(BaseModel):
    product_id: int
    name: str
    category: str
    price: int


class Feedback(BaseModel):
    name: str
    message: str
