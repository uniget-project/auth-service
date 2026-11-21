import uuid
from typing import Protocol, runtime_checkable

from app.models.users import User


@runtime_checkable
class IPasswordHasher(Protocol):
    def hash(self, plain: str) -> str: ...
    def verify(self, plain: str, hashed: str) -> bool: ...
