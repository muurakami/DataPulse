from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    age: int | None = None
    salary: int
    score: float | None = None
