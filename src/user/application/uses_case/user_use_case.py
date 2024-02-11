from typing import List

from user.application.dtos.user_dto.user_dto import UserDto
from user.application.dtos.user_dto.create_user_dto import CreateUserDto
from user.domain.interfaces.user_repository import IUserRepository
from user.domain.entities.user_entity import UserEntity
from user.domain.services.user_service import UserService


class UserUserCase():
    def __init__(self, user_repository: IUserRepository):
        print('User use case')
        self.user_service = UserService(user_repository)
        
    def list_users(self) -> List[UserDto]:
        users = []
        for user in self.user_service.list_users():
            users.append(UserDto(id=str(user.id), nickname=user.nickname, created_at=user.created_at))
        return users
    
    def create_user(self, nickname: str, password: str) -> UserDto:
        new_user = self.user_service.create_user(nickname=nickname, password=password)
        return UserDto(id=str(new_user.id), nickname=new_user.nickname, created_at=new_user.created_at)