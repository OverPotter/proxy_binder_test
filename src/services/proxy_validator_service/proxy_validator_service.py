import asyncio

from aiohttp import ClientError, ClientSession

from src.services.logging_service.logging_service import Logger
from src.services.proxy_validator_service.abc import IProxyValidator


class ProxyValidator(IProxyValidator):
    def __init__(self, check_url: str, logger: Logger):
        self.check_url = check_url
        self.logger = logger

    async def is_proxy_valid(self, proxy: str, session: ClientSession) -> bool:
        ip, port, username, password = proxy.split(":")
        proxy_url = f"http://{username}:{password}@{ip}:{port}"
        self.logger.debug(f"Checking proxy: {proxy_url}")

        try:
            async with session.get(
                self.check_url, proxy=f"http://{proxy_url}", timeout=5
            ) as response:
                valid = response.status == 200
                self.logger.info(f"Proxy {proxy} is {'valid' if valid else 'invalid'}")
                return valid
        except (ClientError, asyncio.TimeoutError) as e:
            self.logger.error(f"Proxy {proxy} failed with error: {e}")
            return False
