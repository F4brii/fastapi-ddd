from pydantic import BaseModel


class CreateUserDto(BaseModel):
    nickname: str
    password: str