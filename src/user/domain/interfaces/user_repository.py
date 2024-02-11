from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def list_users(self):
        pass

    @abstractmethod
    def create_user(self):
        pass