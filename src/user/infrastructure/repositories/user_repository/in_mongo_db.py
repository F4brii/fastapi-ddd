from typing import List

from user.domain.entities.user_entity import UserEntity
from user.domain.interfaces.user_repository import IUserRepository
from user.infrastructure.models.user_model import UserModel
from user.infrastructure.config.data_base.mongo import connection

class InMongoDb(IUserRepository):
    def __init__(self):
        print('User repository')
        
    def list_users(self) -> List[UserEntity]:
        users = connection.local.user.find()
        registered_users = []
        for user in list(users):
            user_entity = UserEntity(id=user['id'], nickname=user['nickname'], password=user['password'], created_at=user['created_at'])
            registered_users.append(user_entity)
        
        return list(registered_users)
    
    def create_user(self, nickname: str, password: str) -> UserEntity:
        new_user = UserModel(nickname=nickname, password=password)
        connection.local.user.insert_one(dict(new_user))
        return UserEntity.from_model(new_user)