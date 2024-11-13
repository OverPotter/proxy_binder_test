from typing import List

from aiofiles import open as aio_open

from src.services.file_manager_service.abc import IFileManager
from src.services.logging_service.logging_service import Logger


class FileManager(IFileManager):
    def __init__(self, logger: Logger):
        self.logger = logger

    async def load_file(self, file_path: str) -> List[str]:
        self.logger.debug(f"Loading file: {file_path}")
        async with aio_open(file_path, "r") as file:
            return [line.strip() for line in await file.readlines() if line.strip()]

    async def append_to_file(self, file_path: str, data: str) -> None:
        self.logger.debug(f"Appending to file: {file_path} | Data: {data}")
        async with aio_open(file_path, "a") as file:
            await file.write(data + "\n")
