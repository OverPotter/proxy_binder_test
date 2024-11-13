from abc import ABC, abstractmethod

from aiohttp import ClientSession


class IProxyValidator(ABC):
    @abstractmethod
    async def is_proxy_valid(self, proxy: str, session: ClientSession) -> bool:
        pass
