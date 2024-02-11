from typing import List

from user.domain.interfaces.user_repository import IUserRepository
from user.domain.entities.user_entity import UserEntity


class UserService():
    def __init__(self, user_repository: IUserRepository):
        print('User service.')
        self.user_repository = user_repository

    def list_users(self) -> List[UserEntity]:
        list_users = self.user_repository.list_users()
        return list_users
    
    def create_user(self, nickname: str, password: str) -> UserEntity:
        return self.user_repository.create_user(nickname=nickname, password=password)
