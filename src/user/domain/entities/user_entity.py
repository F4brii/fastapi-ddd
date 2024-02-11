from datetime import datetime


class UserEntity:
    def __init__(self, id: str, nickname: str, password: str, created_at: datetime):
        self.id = id
        self.nickname = nickname
        self.password = password
        self.created_at = created_at

    @staticmethod
    def from_model(user_model):
        return UserEntity(
            id=user_model.id,
            nickname=user_model.nickname,
            password=user_model.password,
            created_at=user_model.created_at
        )
