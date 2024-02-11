import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    id: Optional[str]
    nickname: str
    password: str
    created_at: Optional[datetime]

    def __init__(self, nickname: str, password: str, id: Optional[str] = None, created_at: Optional[datetime] = None, **kwargs):
        super().__init__(nickname=nickname, password=password, id=id, created_at=created_at, **kwargs)
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.created_at is None:
            self.created_at = datetime.now()

    @staticmethod
    def from_entity(user_entity):
        return UserModel(
            id=user_entity.id,
            nickname=user_entity.nickname,
            password=user_entity.password,
            created_at=user_entity.created_at
        )
