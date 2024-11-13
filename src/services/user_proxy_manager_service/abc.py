from abc import ABC, abstractmethod
from typing import List, Optional

from aiohttp import ClientSession

from src.services.proxy_validator_service.abc import IProxyValidator


class IUserProxyManager(ABC):
    @abstractmethod
    async def assign_proxy(
        self,
        email: str,
        proxies: List[str],
        validator: IProxyValidator,
        session: ClientSession,
    ) -> Optional[str]:
        pass
