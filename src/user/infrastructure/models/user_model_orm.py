import uuid

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Float, DateTime

from user.infrastructure.config.orm.sqlalchemy import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, unique=True,
                default=str(uuid.uuid4()))
    nickname = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    def __init__(self, nickname: str, password: str):
        self.id = str(uuid.uuid4())
        self.nickname = nickname
        self.password = password
        self.created_at = datetime.now()

    @staticmethod
    def from_entity(user_entity):
        return UserModel(
            id=user_entity.id,
            nickname=user_entity.nickname,
            password=user_entity.password,
            created_at=user_entity.created_at
        )
