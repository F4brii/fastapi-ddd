from datetime import datetime
from pydantic import BaseModel


class UserDto(BaseModel):
    id: str
    nickname: str
    created_at: datetime