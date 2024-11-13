from abc import ABC, abstractmethod
from typing import List


class IFileManager(ABC):
    @abstractmethod
    async def load_file(self, file_path: str) -> List[str]:
        pass

    @abstractmethod
    async def append_to_file(self, file_path: str, data: str) -> None:
        pass
