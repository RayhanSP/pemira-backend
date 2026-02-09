from abc import ABC, abstractmethod


class IAuthProvider(ABC):
    @abstractmethod
    def generate_token(self) -> str:
        raise NotImplementedError

