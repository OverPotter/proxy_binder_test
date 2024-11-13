from abc import ABC, abstractmethod
from typing import List

from aiohttp import ClientSession

from src.services.proxy_validator_service.abc import IProxyValidator


class IUserProcessor(ABC):
    @abstractmethod
    async def process_user(
        self,
        email: str,
        proxies: List[str],
        validator: IProxyValidator,
        session: ClientSession,
    ) -> None:
        pass
