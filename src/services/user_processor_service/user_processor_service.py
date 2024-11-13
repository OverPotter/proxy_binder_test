import asyncio
from typing import List

from aiohttp import ClientSession

from src.services.logging_service.logging_service import Logger
from src.services.proxy_validator_service.abc import IProxyValidator
from src.services.user_processor_service.abc import IUserProcessor
from src.services.user_proxy_manager_service.abc import IUserProxyManager


class UserProcessor(IUserProcessor):
    def __init__(
        self, user_proxy_manager: IUserProxyManager, check_interval: int, logger: Logger
    ):
        self.user_proxy_manager = user_proxy_manager
        self.check_interval = check_interval
        self.logger = logger

    async def process_user(
        self,
        email: str,
        proxies: List[str],
        validator: IProxyValidator,
        session: ClientSession,
    ) -> None:
        while True:
            proxy = await self.user_proxy_manager.assign_proxy(
                email, proxies, validator, session
            )
            if proxy:
                self.logger.info(f"Processing {email} with proxy {proxy}")
                await asyncio.sleep(self.check_interval)
