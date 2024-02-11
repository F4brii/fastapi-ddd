from typing import List

from user.domain.entities.user_entity import UserEntity
from user.domain.interfaces.user_repository import IUserRepository
from user.infrastructure.models.user_model import UserModel


class InExecutionTime(IUserRepository):    
    def __init__(self):
        print('User repository')
        self.users: List[UserModel] = [UserModel(nickname='fabricio', password='123456')]
        print(self.users)

    def list_users(self) -> List[UserEntity]:
        print('List users')
        registered_users = []
        for user in list(self.users):
            registered_users.append(UserEntity.from_model(user))
        return registered_users
    
    def create_user(self, nickname: str, password: str) -> UserEntity:
        new_user = UserModel(nickname=nickname, password=password)
        self.users.append(new_user)
        return UserEntity.from_model(new_user)
