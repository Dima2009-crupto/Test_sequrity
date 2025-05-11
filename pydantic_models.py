from typing import Optional

from pydantic import Field, BaseModel


class UserModelResponse(BaseModel):
    name: Optional[str] = Field(None, description="Ім'я користувача")
    email: str = Field(...)
    password: str = Field(...)


class UserModel(UserModelResponse):
    password: str = Field(...)