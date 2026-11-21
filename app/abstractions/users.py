import uuid
from typing import runtime_checkable, Protocol
from app.models.users import User


@runtime_checkable
class IUserRepository(Protocol):
    async def add(
        self,
        *,
        email: str,
        username: str,
        password_hash: str,
        is_staff: bool = False,
    ) -> User: ...

    async def get_by_id(self, user_id: uuid.UUID) -> User | None: ...
    async def get_by_username(self, username: str) -> User | None: ...
    async def get_by_email(self, email: str) -> User | None: ...
    async def exists_by_email_or_username(self, email: str, username: str) -> bool: ...
