from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    name: str
    email: str
    phone: str

class CreateSavingSchema(BaseModel):
    amount: int
    user_id: int
