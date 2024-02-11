from typing import List
from fastapi import APIRouter

from user.application.dtos.user_dto.user_dto import UserDto
from user.application.dtos.user_dto.create_user_dto import CreateUserDto
from user.application.uses_case.user_use_case import UserUserCase
from user.infrastructure.repositories.user_repository.in_mongo_db import InMongoDb

user_router = APIRouter()
user_repository = InMongoDb()
user_use_case = UserUserCase(user_repository)

@user_router.get('/users')
def list_users() -> List[UserDto]:
    return user_use_case.list_users()

@user_router.post('/users', response_model=UserDto)
def create_user(user: CreateUserDto) -> UserDto:
    return user_use_case.create_user(nickname=user.nickname, password=user.password)