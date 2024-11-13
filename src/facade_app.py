import asyncio

from aiohttp import ClientSession

from src._settings import settings_factory
from src.constants import OUTPUT_FILE_PATH, PROXY_FILE_PATH, USER_FILE_PATH
from src.services.file_manager_service.file_manager_service import FileManager
from src.services.logging_service.logging_service import Logger, logger_factory
from src.services.proxy_validator_service.proxy_validator_service import ProxyValidator
from src.services.user_processor_service.user_processor_service import UserProcessor
from src.services.user_proxy_manager_service.user_proxy_manager_service import (
    UserProxyManager,
)

_logger = logger_factory()
_settings = settings_factory()


class FacadeApp:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.file_manager = FileManager(logger)
        self.proxy_validator = ProxyValidator(_settings.PROXY_CHECK_URL, logger)
        self.user_proxy_manager = UserProxyManager(
            self.file_manager, OUTPUT_FILE_PATH, logger
        )
        self.user_processor = UserProcessor(
            self.user_proxy_manager, _settings.CHECK_INTERVAL, logger
        )

    async def run(self) -> None:
        users = await self.file_manager.load_file(USER_FILE_PATH)
        proxies = await self.file_manager.load_file(PROXY_FILE_PATH)

        self.logger.info("Starting application")
        async with ClientSession() as session:
            tasks = [
                self.user_processor.process_user(
                    email, proxies, self.proxy_validator, session
                )
                for email in users
            ]
            await asyncio.gather(*tasks)


def get_app_factory() -> FacadeApp:
    return FacadeApp(logger=_logger)
