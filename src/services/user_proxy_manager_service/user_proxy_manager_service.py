from typing import List, Optional

from aiohttp import ClientSession

from src.services.file_manager_service.abc import IFileManager
from src.services.logging_service.logging_service import Logger
from src.services.proxy_validator_service.abc import IProxyValidator
from src.services.user_proxy_manager_service.abc import IUserProxyManager


class UserProxyManager(IUserProxyManager):
    def __init__(self, file_manager: IFileManager, output_file: str, logger: Logger):
        self.file_manager = file_manager
        self.output_file = output_file
        self.logger = logger
        self.mapping: dict[str, str] = {}

    async def assign_proxy(
        self,
        email: str,
        proxies: List[str],
        validator: IProxyValidator,
        session: ClientSession,
    ) -> Optional[str]:
        for proxy in proxies:
            if await validator.is_proxy_valid(proxy, session):
                self.mapping[email] = proxy
                await self.file_manager.append_to_file(
                    self.output_file, f"{email} -> {proxy}"
                )
                self.logger.info(f"Assigned proxy {proxy} to {email}")
                return proxy
        self.logger.warning(f"No valid proxies available for {email}")
        return None
